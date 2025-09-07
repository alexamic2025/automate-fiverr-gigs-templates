#!/usr/bin/env python3
"""
Fiverr Workflow Automation System
Automates client communication, project tracking, and report generation
"""

import os
import json
import sqlite3
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from typing import Dict, List, Any, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FiverrWorkflowAutomation:
    def __init__(self, db_path: str = "fiverr_business.db"):
        self.db_path = db_path
        self.init_database()
        self.templates_dir = Path("customized_templates")
        
    def init_database(self):
        """Initialize SQLite database for tracking projects and clients"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create clients table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                fiverr_username TEXT,
                first_contact_date TEXT,
                total_projects INTEGER DEFAULT 0,
                total_revenue REAL DEFAULT 0,
                satisfaction_rating INTEGER,
                notes TEXT
            )
        ''')
        
        # Create projects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER,
                project_type TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'pending',
                start_date TEXT,
                due_date TEXT,
                completion_date TEXT,
                package_type TEXT,
                price REAL,
                requirements TEXT,
                deliverables TEXT,
                notes TEXT,
                FOREIGN KEY (client_id) REFERENCES clients (id)
            )
        ''')
        
        # Create communications table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS communications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER,
                client_id INTEGER,
                message_type TEXT,
                subject TEXT,
                content TEXT,
                sent_date TEXT,
                response_required BOOLEAN DEFAULT 0,
                FOREIGN KEY (project_id) REFERENCES projects (id),
                FOREIGN KEY (client_id) REFERENCES clients (id)
            )
        ''')
        
        # Create templates table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                subject TEXT,
                content TEXT,
                variables TEXT,
                usage_count INTEGER DEFAULT 0
            )
        ''')
        
        conn.commit()
        conn.close()
        logger.info("Database initialized successfully")
    
    def add_client(self, name: str, email: str, fiverr_username: str = None) -> int:
        """Add a new client to the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO clients (name, email, fiverr_username, first_contact_date)
            VALUES (?, ?, ?, ?)
        ''', (name, email, fiverr_username, datetime.now().isoformat()))
        
        client_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        logger.info(f"Added new client: {name} (ID: {client_id})")
        return client_id
    
    def create_project(self, client_id: int, project_type: str, title: str, 
                      package_type: str, price: float, due_days: int = 7) -> int:
        """Create a new project"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        start_date = datetime.now()
        due_date = start_date + timedelta(days=due_days)
        
        cursor.execute('''
            INSERT INTO projects (client_id, project_type, title, package_type, 
                                price, start_date, due_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'active')
        ''', (client_id, project_type, title, package_type, price, 
              start_date.isoformat(), due_date.isoformat()))
        
        project_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        logger.info(f"Created new project: {title} (ID: {project_id})")
        return project_id
    
    def get_template(self, template_name: str) -> Optional[Dict[str, Any]]:
        """Get a communication template"""
        templates = {
            'initial_inquiry': {
                'subject': 'Thank you for your interest in my {service_type} services',
                'content': '''Hi {client_name},

Thank you for your interest in my {service_type} services! I'm excited to help you achieve your business goals.

With my extensive experience in data analytics and business intelligence, I deliver results that drive real business impact.

To provide the best recommendations, could you please share:
• Your industry and business objectives
• Specific requirements or challenges
• Timeline for completion
• Any existing data or materials

I typically respond within 1-2 hours and would love to discuss your project in detail.

Looking forward to working with you!

Best regards,
{seller_name}'''
            },
            'project_kickoff': {
                'subject': 'Project Kickoff - {project_title}',
                'content': '''Hi {client_name},

Great! I'm excited to start working on your {project_type} project. Here's what happens next:

**Project Details:**
- Project: {project_title}
- Package: {package_type}
- Delivery Date: {due_date}

**Next Steps:**
1. I'll send you a detailed questionnaire within 2 hours
2. Once completed, I'll begin the analysis/research
3. I'll provide progress updates every 24-48 hours
4. Final delivery will be on {due_date}

**What You Can Expect:**
✅ Professional, comprehensive analysis
✅ Clear, actionable recommendations
✅ Regular communication throughout the project
✅ High-quality deliverables that exceed expectations

If you have any questions or additional requirements, please let me know immediately.

Let's create something amazing together!

Best regards,
{seller_name}'''
            },
            'progress_update': {
                'subject': 'Progress Update - {project_title}',
                'content': '''Hi {client_name},

I wanted to provide you with a quick update on your {project_type} project.

**Current Status:**
- Project is {progress_percentage}% complete
- Currently working on: {current_task}
- On track for delivery: {due_date}

**Completed This Week:**
{completed_tasks}

**Next Steps:**
{next_steps}

If you have any questions or need clarification on anything, please don't hesitate to reach out.

Best regards,
{seller_name}'''
            },
            'delivery_notification': {
                'subject': 'Project Complete - {project_title}',
                'content': '''Hi {client_name},

Excellent news! Your {project_type} project is now complete and ready for delivery.

**What's Included:**
{deliverables_list}

**Key Findings:**
{key_findings}

**Next Steps:**
1. Please review all deliverables
2. Let me know if you need any clarifications
3. I'm available for a follow-up call if needed

I'm confident these insights will drive significant value for your business. Please don't hesitate to reach out if you have any questions.

Thank you for choosing my services!

Best regards,
{seller_name}'''
            },
            'follow_up': {
                'subject': 'Following up on your {project_type} project',
                'content': '''Hi {client_name},

I hope you've had a chance to review the {project_type} deliverables I sent last week.

I wanted to follow up to see:
• How are you finding the recommendations?
• Do you need any clarification or additional analysis?
• Are there any follow-up projects I can help with?

**Additional Services That Might Interest You:**
• Monthly performance monitoring
• Implementation support
• Advanced analytics and forecasting
• Strategic planning sessions

I'm here to support your continued success. Please let me know if there's anything else I can help with.

Best regards,
{seller_name}'''
            }
        }
        
        return templates.get(template_name)
    
    def send_automated_message(self, project_id: int, template_name: str, 
                             custom_vars: Dict[str, str] = None) -> bool:
        """Send an automated message using a template"""
        try:
            # Get project and client details
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT p.*, c.name, c.email 
                FROM projects p 
                JOIN clients c ON p.client_id = c.id 
                WHERE p.id = ?
            ''', (project_id,))
            
            result = cursor.fetchone()
            if not result:
                logger.error(f"Project {project_id} not found")
                return False
            
            # Map database columns to variables
            project_data = {
                'project_id': result[0],
                'client_id': result[1],
                'project_type': result[2],
                'project_title': result[3],
                'package_type': result[6],
                'due_date': result[8],
                'client_name': result[11],
                'client_email': result[12]
            }
            
            # Get template
            template = self.get_template(template_name)
            if not template:
                logger.error(f"Template {template_name} not found")
                return False
            
            # Add default seller information
            project_data.update({
                'seller_name': 'Your Name',
                'service_type': project_data['project_type']
            })
            
            # Merge custom variables
            if custom_vars:
                project_data.update(custom_vars)
            
            # Format template
            try:
                subject = template['subject'].format(**project_data)
                content = template['content'].format(**project_data)
            except KeyError as e:
                logger.error(f"Missing template variable: {e}")
                return False
            
            # Log the communication (in real implementation, this would send email)
            cursor.execute('''
                INSERT INTO communications (project_id, client_id, message_type, 
                                          subject, content, sent_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (project_id, project_data['client_id'], template_name, 
                  subject, content, datetime.now().isoformat()))
            
            conn.commit()
            conn.close()
            
            logger.info(f"Automated message sent: {template_name} for project {project_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error sending automated message: {str(e)}")
            return False
    
    def update_project_status(self, project_id: int, status: str, notes: str = None):
        """Update project status and trigger appropriate communications"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Update project status
        cursor.execute('''
            UPDATE projects SET status = ?, notes = ? WHERE id = ?
        ''', (status, notes, project_id))
        
        conn.commit()
        conn.close()
        
        # Trigger automated communications based on status
        if status == 'active':
            self.send_automated_message(project_id, 'project_kickoff')
        elif status == 'in_progress':
            self.send_automated_message(project_id, 'progress_update', {
                'progress_percentage': '50',
                'current_task': 'Data analysis and insights generation',
                'completed_tasks': '• Initial research completed\\n• Data collection finalized',
                'next_steps': '• Complete analysis\\n• Generate recommendations\\n• Prepare final report'
            })
        elif status == 'completed':
            self.send_automated_message(project_id, 'delivery_notification', {
                'deliverables_list': '• Comprehensive analysis report\\n• Executive summary\\n• Data visualizations\\n• Strategic recommendations',
                'key_findings': 'Key insights and actionable recommendations included in the full report.'
            })
            # Schedule follow-up
            self.schedule_follow_up(project_id, days=7)
        
        logger.info(f"Project {project_id} status updated to: {status}")
    
    def schedule_follow_up(self, project_id: int, days: int = 7):
        """Schedule a follow-up communication"""
        # In a real implementation, this would use a task scheduler
        # For now, we'll just log the scheduled follow-up
        follow_up_date = datetime.now() + timedelta(days=days)
        logger.info(f"Follow-up scheduled for project {project_id} on {follow_up_date.date()}")
    
    def generate_project_report(self, project_id: int) -> Dict[str, Any]:
        """Generate a project status report"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get project details
        cursor.execute('''
            SELECT p.*, c.name, c.email 
            FROM projects p 
            JOIN clients c ON p.client_id = c.id 
            WHERE p.id = ?
        ''', (project_id,))
        
        project = cursor.fetchone()
        
        # Get communications
        cursor.execute('''
            SELECT message_type, subject, sent_date 
            FROM communications 
            WHERE project_id = ? 
            ORDER BY sent_date DESC
        ''', (project_id,))
        
        communications = cursor.fetchall()
        conn.close()
        
        if not project:
            return {}
        
        return {
            'project_id': project[0],
            'client_name': project[11],
            'project_type': project[2],
            'title': project[3],
            'status': project[5],
            'start_date': project[7],
            'due_date': project[8],
            'price': project[10],
            'communications': [
                {
                    'type': comm[0],
                    'subject': comm[1],
                    'date': comm[2]
                } for comm in communications
            ]
        }
    
    def get_dashboard_data(self) -> Dict[str, Any]:
        """Get data for the business dashboard"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get project statistics
        cursor.execute('SELECT COUNT(*) FROM projects')
        total_projects = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM projects WHERE status = "active"')
        active_projects = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM projects WHERE status = "completed"')
        completed_projects = cursor.fetchone()[0]
        
        cursor.execute('SELECT SUM(price) FROM projects WHERE status = "completed"')
        total_revenue = cursor.fetchone()[0] or 0
        
        cursor.execute('SELECT COUNT(*) FROM clients')
        total_clients = cursor.fetchone()[0]
        
        # Get recent projects
        cursor.execute('''
            SELECT p.id, p.title, p.status, p.due_date, c.name 
            FROM projects p 
            JOIN clients c ON p.client_id = c.id 
            ORDER BY p.start_date DESC 
            LIMIT 10
        ''')
        recent_projects = cursor.fetchall()
        
        conn.close()
        
        return {
            'total_projects': total_projects,
            'active_projects': active_projects,
            'completed_projects': completed_projects,
            'total_revenue': total_revenue,
            'total_clients': total_clients,
            'recent_projects': [
                {
                    'id': p[0],
                    'title': p[1],
                    'status': p[2],
                    'due_date': p[3],
                    'client_name': p[4]
                } for p in recent_projects
            ]
        }

def main():
    """Demo of the workflow automation system"""
    print("🤖 Fiverr Workflow Automation System")
    print("=" * 50)
    
    # Initialize the system
    automation = FiverrWorkflowAutomation()
    
    # Demo: Add a client and project
    client_id = automation.add_client("John Smith", "john@example.com", "johnsmith_fiverr")
    project_id = automation.create_project(
        client_id=client_id,
        project_type="Market Research",
        title="E-commerce Market Analysis",
        package_type="Standard",
        price=599.0,
        due_days=7
    )
    
    # Demo: Update project status (triggers automated communications)
    automation.update_project_status(project_id, "active")
    automation.update_project_status(project_id, "in_progress")
    automation.update_project_status(project_id, "completed")
    
    # Generate project report
    report = automation.generate_project_report(project_id)
    print(f"\n📊 Project Report for: {report['title']}")
    print(f"Client: {report['client_name']}")
    print(f"Status: {report['status']}")
    print(f"Communications sent: {len(report['communications'])}")
    
    # Get dashboard data
    dashboard = automation.get_dashboard_data()
    print(f"\n📈 Business Dashboard:")
    print(f"Total Projects: {dashboard['total_projects']}")
    print(f"Active Projects: {dashboard['active_projects']}")
    print(f"Total Revenue: ${dashboard['total_revenue']}")
    print(f"Total Clients: {dashboard['total_clients']}")
    
    print("\n✅ Workflow automation demo completed!")

if __name__ == "__main__":
    main()


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    fiverr_username = db.Column(db.String(50))
    first_contact_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_projects = db.Column(db.Integer, default=0)
    total_revenue = db.Column(db.Float, default=0.0)
    satisfaction_rating = db.Column(db.Integer)
    notes = db.Column(db.Text)
    
    # Relationship
    projects = db.relationship('Project', backref='client', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'fiverr_username': self.fiverr_username,
            'first_contact_date': self.first_contact_date.isoformat() if self.first_contact_date else None,
            'total_projects': self.total_projects,
            'total_revenue': self.total_revenue,
            'satisfaction_rating': self.satisfaction_rating,
            'notes': self.notes
        }

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    project_type = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    completion_date = db.Column(db.DateTime)
    package_type = db.Column(db.String(20))
    price = db.Column(db.Float)
    requirements = db.Column(db.Text)
    deliverables = db.Column(db.Text)
    notes = db.Column(db.Text)
    progress = db.Column(db.Integer, default=0)
    
    # Relationship
    communications = db.relationship('Communication', backref='project', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'client_name': self.client.name if self.client else None,
            'project_type': self.project_type,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completion_date': self.completion_date.isoformat() if self.completion_date else None,
            'package_type': self.package_type,
            'price': self.price,
            'requirements': self.requirements,
            'deliverables': self.deliverables,
            'notes': self.notes,
            'progress': self.progress
        }

class Communication(db.Model):
    __tablename__ = 'communications'
    
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    message_type = db.Column(db.String(50))
    subject = db.Column(db.String(200))
    content = db.Column(db.Text)
    sent_date = db.Column(db.DateTime, default=datetime.utcnow)
    response_required = db.Column(db.Boolean, default=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'client_id': self.client_id,
            'message_type': self.message_type,
            'subject': self.subject,
            'content': self.content,
            'sent_date': self.sent_date.isoformat() if self.sent_date else None,
            'response_required': self.response_required
        }

class Template(db.Model):
    __tablename__ = 'templates'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    subject = db.Column(db.String(200))
    content = db.Column(db.Text)
    variables = db.Column(db.Text)  # JSON string of variables
    usage_count = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'subject': self.subject,
            'content': self.content,
            'variables': self.variables,
            'usage_count': self.usage_count,
            'created_date': self.created_date.isoformat() if self.created_date else None
        }


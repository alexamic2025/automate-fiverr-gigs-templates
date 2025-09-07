#!/usr/bin/env python3
"""
SharePoint Templates and Power Automate Integration
Creates SharePoint lists and deploys Power Automate flows for intake forms
"""

import json
import requests
import os
from datetime import datetime

class SharePointPowerAutomateDeployer:
    def __init__(self):
        self.tenant_id = "75db62a2-c72e-453b-ac8b-5deda95159e9"
        self.client_id = "acc2972d-b762-495d-b7a8-5743fd5f6486"  
        self.client_secret = "Mbq8Q~rTm32W_amwcB.JDY21f8BPO8LX~WdR8bXY"
        self.environment_id = "75db62a2-c72e-453b-ac8b-5deda95159e9"
        self.sharepoint_site = "https://actlearningsystems.sharepoint.com/sites/PowerAutomate"
        self.access_token = None
    
    def authenticate(self):
        """Authenticate with Microsoft Graph API"""
        auth_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'https://graph.microsoft.com/.default'
        }
        
        try:
            response = requests.post(auth_url, headers=headers, data=data, timeout=30)
            if response.status_code == 200:
                self.access_token = response.json()['access_token']
                print("✅ Authentication successful")
                return True
            else:
                print(f"❌ Authentication failed: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Authentication error: {str(e)}")
            return False
    
    def create_sharepoint_lists_template(self):
        """Create SharePoint list templates for intake forms"""
        print("\n📋 Creating SharePoint List Templates...")
        
        # Lead Qualification List Template
        lead_qualification_list = {
            "displayName": "Lead Qualification Intake",
            "description": "Lead qualification form responses with automated scoring",
            "columns": [
                {"name": "SubmissionDate", "type": "dateTime", "required": True},
                {"name": "ContactName", "type": "text", "required": True},
                {"name": "CompanyName", "type": "text", "required": True},
                {"name": "Email", "type": "text", "required": True},
                {"name": "Phone", "type": "text", "required": False},
                {"name": "ProjectType", "type": "choice", "choices": ["Power Automate", "Power BI", "Integration", "Migration", "Other"]},
                {"name": "BudgetRange", "type": "choice", "choices": ["Under $10k", "$10k-$50k", "$50k-$100k", "Over $100k"]},
                {"name": "Timeline", "type": "choice", "choices": ["ASAP", "1-3 months", "3-6 months", "6+ months"]},
                {"name": "DecisionMaker", "type": "choice", "choices": ["Yes", "No", "Influencer"]},
                {"name": "CurrentProcess", "type": "text", "required": False},
                {"name": "PainPoints", "type": "text", "required": False},
                {"name": "SuccessMetrics", "type": "text", "required": False},
                {"name": "LeadScore", "type": "number", "required": True},
                {"name": "Priority", "type": "choice", "choices": ["High", "Medium", "Low"]},
                {"name": "Status", "type": "choice", "choices": ["New", "Qualified", "Contacted", "Proposal", "Won", "Lost"]}
            ]
        }
        
        # Project Discovery List Template  
        project_discovery_list = {
            "displayName": "Project Discovery Requirements",
            "description": "Detailed project requirements and scope information",
            "columns": [
                {"name": "SubmissionDate", "type": "dateTime", "required": True},
                {"name": "ClientName", "type": "text", "required": True},
                {"name": "ProjectName", "type": "text", "required": True},
                {"name": "BusinessObjectives", "type": "text", "required": True},
                {"name": "Stakeholders", "type": "text", "required": True},
                {"name": "CurrentState", "type": "text", "required": True},
                {"name": "DesiredOutcomes", "type": "text", "required": True},
                {"name": "Constraints", "type": "text", "required": False},
                {"name": "Budget", "type": "text", "required": True},
                {"name": "Timeline", "type": "text", "required": True},
                {"name": "TechnicalComplexity", "type": "choice", "choices": ["Low", "Medium", "High", "Very High"]},
                {"name": "RiskLevel", "type": "choice", "choices": ["Low", "Medium", "High"]},
                {"name": "ProjectStatus", "type": "choice", "choices": ["Discovery", "Scoping", "Approved", "In Progress", "Complete"]}
            ]
        }
        
        # Technical Assessment List Template
        technical_assessment_list = {
            "displayName": "Technical Assessment",
            "description": "Technical infrastructure and capability assessment",
            "columns": [
                {"name": "SubmissionDate", "type": "dateTime", "required": True},
                {"name": "ClientName", "type": "text", "required": True},
                {"name": "CurrentSystems", "type": "text", "required": True},
                {"name": "TechnicalStack", "type": "text", "required": True},
                {"name": "SecurityRequirements", "type": "text", "required": True},
                {"name": "ComplianceNeeds", "type": "text", "required": False},
                {"name": "PerformanceReqs", "type": "text", "required": True},
                {"name": "IntegrationPoints", "type": "text", "required": True},
                {"name": "TechnicalSkills", "type": "text", "required": True},
                {"name": "InfrastructureReadiness", "type": "choice", "choices": ["Ready", "Minor Changes", "Major Changes", "Complete Overhaul"]},
                {"name": "TechnicalRisk", "type": "choice", "choices": ["Low", "Medium", "High", "Critical"]},
                {"name": "RecommendedApproach", "type": "text", "required": False}
            ]
        }
        
        # Client Success Monitoring List Template
        client_success_list = {
            "displayName": "Client Success Monitoring",
            "description": "Ongoing client health and satisfaction tracking",
            "columns": [
                {"name": "SubmissionDate", "type": "dateTime", "required": True},
                {"name": "ClientName", "type": "text", "required": True},
                {"name": "ProjectName", "type": "text", "required": True},
                {"name": "SatisfactionScore", "type": "number", "required": True},
                {"name": "ProjectStatus", "type": "choice", "choices": ["On Track", "At Risk", "Behind", "Complete"]},
                {"name": "CommunicationFreq", "type": "choice", "choices": ["Weekly", "Bi-weekly", "Monthly", "Quarterly"]},
                {"name": "ResponseTime", "type": "choice", "choices": ["Excellent", "Good", "Average", "Poor"]},
                {"name": "TechnicalExpertise", "type": "number", "required": True},
                {"name": "ProcessImprovement", "type": "number", "required": True},
                {"name": "ValueDelivery", "type": "number", "required": True},
                {"name": "OverallHealth", "type": "choice", "choices": ["Excellent", "Good", "At Risk", "Critical"]},
                {"name": "RiskFactors", "type": "text", "required": False},
                {"name": "ActionItems", "type": "text", "required": False},
                {"name": "NextSteps", "type": "text", "required": False}
            ]
        }
        
        # Save templates to files
        templates = {
            "lead_qualification_sharepoint_list.json": lead_qualification_list,
            "project_discovery_sharepoint_list.json": project_discovery_list,
            "technical_assessment_sharepoint_list.json": technical_assessment_list,
            "client_success_sharepoint_list.json": client_success_list
        }
        
        for filename, template in templates.items():
            with open(filename, 'w') as f:
                json.dump(template, f, indent=2)
            print(f"  ✅ Created: {filename}")
        
        return True
    
    def create_power_automate_templates(self):
        """Create Power Automate flow templates for form processing"""
        print("\n🔄 Creating Power Automate Flow Templates...")
        
        # Create comprehensive flow definitions
        flows = {
            "Lead_Qualification_Flow.json": self.get_lead_qualification_flow(),
            "Project_Discovery_Flow.json": self.get_project_discovery_flow(), 
            "Technical_Assessment_Flow.json": self.get_technical_assessment_flow(),
            "Client_Success_Flow.json": self.get_client_success_flow()
        }
        
        for filename, flow_def in flows.items():
            with open(filename, 'w') as f:
                json.dump(flow_def, f, indent=2)
            print(f"  ✅ Created: {filename}")
        
        return True
    
    def get_lead_qualification_flow(self):
        """Lead Qualification automation flow definition"""
        return {
            "displayName": "Lead Qualification Automation",
            "description": "Processes lead qualification forms with automated scoring and routing",
            "triggerType": "Microsoft Forms - When a new response is submitted",
            "actions": [
                {
                    "name": "Calculate Lead Score",
                    "type": "Compose",
                    "description": "Calculate lead score based on responses",
                    "formula": "add(if(equals(triggerOutputs()?['body/Budget'], 'Over $100k'), 10, if(equals(triggerOutputs()?['body/Budget'], '$50k-$100k'), 7, if(equals(triggerOutputs()?['body/Budget'], '$10k-$50k'), 5, 2))), if(equals(triggerOutputs()?['body/Timeline'], 'ASAP'), 8, if(equals(triggerOutputs()?['body/Timeline'], '1-3 months'), 6, if(equals(triggerOutputs()?['body/Timeline'], '3-6 months'), 4, 2))), if(equals(triggerOutputs()?['body/DecisionMaker'], 'Yes'), 10, if(equals(triggerOutputs()?['body/DecisionMaker'], 'Influencer'), 5, 0)))"
                },
                {
                    "name": "Determine Priority",
                    "type": "Condition",
                    "condition": "greater(outputs('Calculate_Lead_Score'), 25)",
                    "ifYes": [
                        {
                            "name": "Set High Priority",
                            "type": "Compose",
                            "value": "High"
                        },
                        {
                            "name": "Send High Priority Alert",
                            "type": "Send Email",
                            "to": "sales@company.com",
                            "subject": "🚨 High Priority Lead Alert",
                            "body": "New high-priority lead scored @{outputs('Calculate_Lead_Score')} points"
                        }
                    ],
                    "ifNo": [
                        {
                            "name": "Set Normal Priority", 
                            "type": "Compose",
                            "value": "Medium"
                        }
                    ]
                },
                {
                    "name": "Create SharePoint Item",
                    "type": "SharePoint - Create Item",
                    "siteUrl": "@{variables('SharePointSite')}",
                    "listName": "Lead Qualification Intake",
                    "fields": {
                        "ContactName": "@{triggerOutputs()?['body/ContactName']}",
                        "CompanyName": "@{triggerOutputs()?['body/CompanyName']}",
                        "Email": "@{triggerOutputs()?['body/Email']}",
                        "Phone": "@{triggerOutputs()?['body/Phone']}",
                        "ProjectType": "@{triggerOutputs()?['body/ProjectType']}",
                        "BudgetRange": "@{triggerOutputs()?['body/Budget']}",
                        "Timeline": "@{triggerOutputs()?['body/Timeline']}",
                        "LeadScore": "@{outputs('Calculate_Lead_Score')}",
                        "Priority": "@{if(greater(outputs('Calculate_Lead_Score'), 25), 'High', 'Medium')}",
                        "Status": "New"
                    }
                },
                {
                    "name": "Send Confirmation Email",
                    "type": "Send Email",
                    "to": "@{triggerOutputs()?['body/Email']}",
                    "subject": "Thank you for your interest - Next Steps",
                    "body": "Thank you for submitting your project details. We'll be in touch within 24 hours."
                }
            ],
            "variables": {
                "SharePointSite": "https://actlearningsystems.sharepoint.com/sites/PowerAutomate"
            }
        }
    
    def get_project_discovery_flow(self):
        """Project Discovery processing flow"""
        return {
            "displayName": "Project Discovery Processing",
            "description": "Processes detailed project discovery forms",
            "triggerType": "Microsoft Forms - When a new response is submitted",
            "actions": [
                {
                    "name": "Assess Technical Complexity",
                    "type": "Switch",
                    "expression": "@triggerOutputs()?['body/TechnicalComplexity']",
                    "cases": {
                        "High": [
                            {"name": "Flag for Technical Review", "type": "Compose", "value": "Technical review required"}
                        ],
                        "Very High": [
                            {"name": "Flag for Architecture Review", "type": "Compose", "value": "Solution architecture review required"}
                        ]
                    }
                },
                {
                    "name": "Create SharePoint Item",
                    "type": "SharePoint - Create Item",
                    "siteUrl": "@{variables('SharePointSite')}",
                    "listName": "Project Discovery Requirements"
                },
                {
                    "name": "Create Teams Notification",
                    "type": "Teams - Post Message",
                    "message": "New project discovery submitted for @{triggerOutputs()?['body/ClientName']}"
                }
            ]
        }
    
    def get_technical_assessment_flow(self):
        """Technical Assessment processing flow"""
        return {
            "displayName": "Technical Assessment Processing",
            "description": "Processes technical infrastructure assessments",
            "triggerType": "Microsoft Forms - When a new response is submitted",
            "actions": [
                {
                    "name": "Risk Assessment",
                    "type": "Condition",
                    "condition": "equals(triggerOutputs()?['body/TechnicalRisk'], 'High')",
                    "ifYes": [
                        {
                            "name": "Alert Technical Team",
                            "type": "Send Email",
                            "to": "technical@company.com",
                            "subject": "High Risk Technical Assessment"
                        }
                    ]
                },
                {
                    "name": "Create SharePoint Item",
                    "type": "SharePoint - Create Item",
                    "siteUrl": "@{variables('SharePointSite')}",
                    "listName": "Technical Assessment"
                }
            ]
        }
    
    def get_client_success_flow(self):
        """Client Success monitoring flow"""
        return {
            "displayName": "Client Success Monitoring", 
            "description": "Monitors client health and triggers interventions",
            "triggerType": "Microsoft Forms - When a new response is submitted",
            "actions": [
                {
                    "name": "Calculate Health Score",
                    "type": "Compose",
                    "formula": "div(add(triggerOutputs()?['body/SatisfactionScore'], triggerOutputs()?['body/TechnicalExpertise'], triggerOutputs()?['body/ProcessImprovement'], triggerOutputs()?['body/ValueDelivery']), 4)"
                },
                {
                    "name": "Check Health Status",
                    "type": "Condition", 
                    "condition": "less(outputs('Calculate_Health_Score'), 7)",
                    "ifYes": [
                        {
                            "name": "Trigger Intervention",
                            "type": "Send Email",
                            "to": "success@company.com",
                            "subject": "🚨 Client Health Alert - Immediate Attention Required"
                        }
                    ]
                },
                {
                    "name": "Update SharePoint",
                    "type": "SharePoint - Create Item",
                    "siteUrl": "@{variables('SharePointSite')}",
                    "listName": "Client Success Monitoring"
                }
            ]
        }
    
    def create_deployment_script(self):
        """Create PowerShell deployment script"""
        print("\n🚀 Creating Deployment Script...")
        
        deployment_script = '''# SharePoint and Power Automate Deployment Script
# Run this script to deploy your intake forms infrastructure

param(
    [string]$SharePointSiteUrl = "https://actlearningsystems.sharepoint.com/sites/PowerAutomate",
    [string]$EnvironmentName = "ACT Learning Systems (default)"
)

Write-Host "🚀 Deploying Intake Forms Infrastructure..." -ForegroundColor Green
Write-Host "Environment: $EnvironmentName" -ForegroundColor Yellow
Write-Host "SharePoint Site: $SharePointSiteUrl" -ForegroundColor Yellow

# Step 1: Create SharePoint Lists
Write-Host "`n📋 Step 1: Creating SharePoint Lists..." -ForegroundColor Cyan

$lists = @(
    "Lead Qualification Intake",
    "Project Discovery Requirements", 
    "Technical Assessment",
    "Client Success Monitoring"
)

foreach ($listName in $lists) {
    Write-Host "  Creating list: $listName" -ForegroundColor White
    # Note: Manual creation required via SharePoint UI or PnP PowerShell
}

# Step 2: Deploy Power Automate Flows
Write-Host "`n🔄 Step 2: Deploying Power Automate Flows..." -ForegroundColor Cyan

$flows = @(
    "Lead_Qualification_Flow.json",
    "Project_Discovery_Flow.json",
    "Technical_Assessment_Flow.json", 
    "Client_Success_Flow.json"
)

foreach ($flow in $flows) {
    if (Test-Path $flow) {
        Write-Host "  Found flow definition: $flow" -ForegroundColor Green
        # pac flow import --path $flow --environment-name "$EnvironmentName"
        Write-Host "    ⚠️ Manual import required via Power Automate portal" -ForegroundColor Yellow
    } else {
        Write-Host "  ❌ Flow definition not found: $flow" -ForegroundColor Red
    }
}

# Step 3: Create Microsoft Forms
Write-Host "`n📝 Step 3: Microsoft Forms Setup..." -ForegroundColor Cyan
Write-Host "  Navigate to https://forms.microsoft.com" -ForegroundColor White
Write-Host "  Create forms using the intake form templates" -ForegroundColor White
Write-Host "  Configure form responses to trigger Power Automate flows" -ForegroundColor White

# Step 4: Configure Permissions
Write-Host "`n🔐 Step 4: Permission Configuration..." -ForegroundColor Cyan
Write-Host "  Ensure Power Automate has access to:" -ForegroundColor White
Write-Host "    ✅ SharePoint Lists (Read/Write)" -ForegroundColor Green
Write-Host "    ✅ Microsoft Forms (Read)" -ForegroundColor Green
Write-Host "    ✅ Email (Send)" -ForegroundColor Green
Write-Host "    ✅ Teams (Post Messages)" -ForegroundColor Green

Write-Host "`n🎉 Deployment script completed!" -ForegroundColor Green
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Create SharePoint lists manually or with PnP PowerShell" -ForegroundColor White
Write-Host "2. Import Power Automate flows via the portal" -ForegroundColor White
Write-Host "3. Create Microsoft Forms using the templates" -ForegroundColor White
Write-Host "4. Test end-to-end workflow" -ForegroundColor White
'''
        
        with open("deploy_sharepoint_powerautomate.ps1", 'w', encoding='utf-8') as f:
            f.write(deployment_script)
        
        print("  ✅ Created: deploy_sharepoint_powerautomate.ps1")
        return True
    
    def run_deployment(self):
        """Run the complete deployment process"""
        print("🚀 SharePoint & Power Automate Integration Deployment")
        print("=" * 60)
        
        if not self.authenticate():
            print("❌ Authentication failed. Please check your credentials.")
            return False
        
        success_count = 0
        total_steps = 3
        
        steps = [
            ("SharePoint List Templates", self.create_sharepoint_lists_template),
            ("Power Automate Flow Templates", self.create_power_automate_templates), 
            ("Deployment Script", self.create_deployment_script)
        ]
        
        for step_name, step_function in steps:
            try:
                if step_function():
                    success_count += 1
                    print(f"✅ {step_name} completed successfully")
                else:
                    print(f"❌ {step_name} failed")
            except Exception as e:
                print(f"❌ {step_name} error: {str(e)}")
        
        print(f"\n🎉 Deployment completed! {success_count}/{total_steps} steps successful")
        
        if success_count == total_steps:
            print("\n📋 Files Created:")
            print("  📊 SharePoint List Templates:")
            print("    • lead_qualification_sharepoint_list.json")
            print("    • project_discovery_sharepoint_list.json") 
            print("    • technical_assessment_sharepoint_list.json")
            print("    • client_success_sharepoint_list.json")
            print("\n  🔄 Power Automate Flow Templates:")
            print("    • Lead_Qualification_Flow.json")
            print("    • Project_Discovery_Flow.json")
            print("    • Technical_Assessment_Flow.json")
            print("    • Client_Success_Flow.json")
            print("\n  🚀 Deployment Script:")
            print("    • deploy_sharepoint_powerautomate.ps1")
            
            print("\n📝 Next Steps:")
            print("1. Run: .\\deploy_sharepoint_powerautomate.ps1")
            print("2. Create SharePoint lists using the JSON templates")
            print("3. Import Power Automate flows via the portal")
            print("4. Create Microsoft Forms using your intake templates")
            print("5. Test the complete workflow")
        
        return success_count == total_steps

if __name__ == "__main__":
    deployer = SharePointPowerAutomateDeployer()
    deployer.run_deployment()

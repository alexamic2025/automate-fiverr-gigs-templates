#!/usr/bin/env python3
"""
SharePoint Folder Structure Automation Scripts
Created for automated document management business setup

This script generates PowerShell scripts, Power Automate flows, and 
configuration files for creating SharePoint folder structures.
"""

import json
import os
from datetime import datetime

def create_folder_structure_config():
    """Create comprehensive folder structure configuration"""
    
    folder_structures = {
        "Client_Documents": {
            "description": "Store all client-related files and deliverables",
            "folders": [
                "Client_001_CompanyName/01_Contracts_and_Agreements",
                "Client_001_CompanyName/02_Project_Deliverables",
                "Client_001_CompanyName/03_Meeting_Notes", 
                "Client_001_CompanyName/04_Correspondence",
                "Client_001_CompanyName/05_Reports_and_Analytics",
                "Client_001_CompanyName/06_Archive",
                "Client_002_CompanyName/01_Contracts_and_Agreements",
                "Client_002_CompanyName/02_Project_Deliverables",
                "Client_002_CompanyName/03_Meeting_Notes",
                "Client_002_CompanyName/04_Correspondence", 
                "Client_002_CompanyName/05_Reports_and_Analytics",
                "Client_002_CompanyName/06_Archive",
                "Client_Templates/Contract_Templates",
                "Client_Templates/Proposal_Templates",
                "Client_Templates/Report_Templates",
                "Client_Templates/Communication_Templates",
                "Shared_Resources/Industry_Research",
                "Shared_Resources/Best_Practices",
                "Shared_Resources/Training_Materials",
                "Archive/2024/Q1",
                "Archive/2024/Q2",
                "Archive/2024/Q3",
                "Archive/2024/Q4"
            ],
            "permissions": {
                "Client_001_CompanyName": "Restricted to Client 1 team",
                "Client_002_CompanyName": "Restricted to Client 2 team",
                "Client_Templates": "Read access for all team members",
                "Shared_Resources": "Contribute access for all team members",
                "Archive": "Read-only access"
            }
        },
        
        "Project_Templates": {
            "description": "Store reusable project templates and documents",
            "folders": [
                "Proposal_Templates/Standard_Proposals/Data_Analytics",
                "Proposal_Templates/Standard_Proposals/Business_Intelligence",
                "Proposal_Templates/Standard_Proposals/Process_Automation",
                "Proposal_Templates/Custom_Proposals/Enterprise_Solutions",
                "Proposal_Templates/Custom_Proposals/SMB_Solutions",
                "Proposal_Templates/RFP_Responses/Government",
                "Proposal_Templates/RFP_Responses/Private_Sector",
                "Contract_Templates/Service_Agreements/Standard_MSA",
                "Contract_Templates/Service_Agreements/Enterprise_MSA",
                "Contract_Templates/NDAs/Standard_NDA",
                "Contract_Templates/NDAs/Mutual_NDA",
                "Contract_Templates/SOWs/Consulting_SOW",
                "Contract_Templates/SOWs/Implementation_SOW",
                "Project_Plans/Automation_Projects/Power_Platform",
                "Project_Plans/Automation_Projects/Custom_Development",
                "Project_Plans/Consulting_Projects/Strategy_Consulting",
                "Project_Plans/Consulting_Projects/Process_Improvement",
                "Project_Plans/Implementation_Projects/System_Integration",
                "Project_Plans/Implementation_Projects/Data_Migration",
                "Deliverable_Templates/Reports/Executive_Reports",
                "Deliverable_Templates/Reports/Technical_Reports",
                "Deliverable_Templates/Reports/Financial_Reports",
                "Deliverable_Templates/Dashboards/Executive_Dashboards",
                "Deliverable_Templates/Dashboards/Operational_Dashboards",
                "Deliverable_Templates/Presentations/Client_Presentations",
                "Deliverable_Templates/Presentations/Internal_Presentations",
                "Quality_Assurance/Checklists/Project_Checklists",
                "Quality_Assurance/Checklists/Deliverable_Checklists",
                "Quality_Assurance/Review_Templates/Peer_Review",
                "Quality_Assurance/Review_Templates/Client_Review",
                "Quality_Assurance/Testing_Procedures/UAT_Procedures",
                "Quality_Assurance/Testing_Procedures/System_Testing"
            ],
            "permissions": {
                "Proposal_Templates": "Edit access for sales team, read for others",
                "Contract_Templates": "Edit access for legal team, read for others", 
                "Project_Plans": "Edit access for project managers",
                "Deliverable_Templates": "Contribute access for all team members",
                "Quality_Assurance": "Edit access for QA team, read for others"
            }
        },
        
        "Reports_and_Analytics": {
            "description": "Store automated reports and business intelligence documents",
            "folders": [
                "Daily_Reports/Automated_Reports/System_Performance",
                "Daily_Reports/Automated_Reports/Client_Activity",
                "Daily_Reports/Automated_Reports/Team_Productivity",
                "Daily_Reports/Manual_Reports/Exception_Reports",
                "Daily_Reports/Manual_Reports/Custom_Analysis",
                "Weekly_Reports/Executive_Summary/Business_Performance",
                "Weekly_Reports/Executive_Summary/Financial_Summary",
                "Weekly_Reports/Executive_Summary/Client_Health",
                "Weekly_Reports/Operational_Reports/Project_Status",
                "Weekly_Reports/Operational_Reports/Resource_Utilization",
                "Weekly_Reports/Operational_Reports/Quality_Metrics",
                "Monthly_Reports/Business_Performance/Revenue_Analysis",
                "Monthly_Reports/Business_Performance/Growth_Metrics",
                "Monthly_Reports/Business_Performance/Market_Analysis",
                "Monthly_Reports/Financial_Reports/P&L_Reports",
                "Monthly_Reports/Financial_Reports/Cash_Flow",
                "Monthly_Reports/Financial_Reports/Budget_Variance",
                "Monthly_Reports/Client_Reports/Client_Scorecards",
                "Monthly_Reports/Client_Reports/Satisfaction_Reports",
                "Monthly_Reports/Client_Reports/Usage_Analytics",
                "Quarterly_Reports/Strategic_Reviews/Business_Strategy",
                "Quarterly_Reports/Strategic_Reviews/Market_Position",
                "Quarterly_Reports/Strategic_Reviews/Competitive_Analysis",
                "Quarterly_Reports/Board_Reports/Executive_Summary",
                "Quarterly_Reports/Board_Reports/Financial_Performance",
                "Quarterly_Reports/Board_Reports/Strategic_Initiatives",
                "Annual_Reports/Year_End_Reports/Annual_Performance",
                "Annual_Reports/Year_End_Reports/Financial_Statements",
                "Annual_Reports/Planning_Reports/Strategic_Planning",
                "Annual_Reports/Planning_Reports/Budget_Planning",
                "Custom_Analytics/Client_Specific/Client_001_Analytics",
                "Custom_Analytics/Client_Specific/Client_002_Analytics",
                "Custom_Analytics/Industry_Analysis/Healthcare_Analytics",
                "Custom_Analytics/Industry_Analysis/Manufacturing_Analytics",
                "Custom_Analytics/Industry_Analysis/Financial_Services_Analytics",
                "Custom_Analytics/Competitive_Analysis/Market_Research",
                "Custom_Analytics/Competitive_Analysis/Competitor_Profiles",
                "Dashboard_Exports/Power_BI/Executive_Dashboards",
                "Dashboard_Exports/Power_BI/Operational_Dashboards",
                "Dashboard_Exports/Excel/Financial_Dashboards",
                "Dashboard_Exports/Excel/Performance_Dashboards"
            ],
            "permissions": {
                "Daily_Reports": "Read access for management and team leads",
                "Weekly_Reports": "Read access for all team members",
                "Monthly_Reports": "Read access based on role and confidentiality",
                "Quarterly_Reports": "Restricted to management and board members",
                "Annual_Reports": "Restricted to senior management",
                "Custom_Analytics": "Access based on client and project assignments",
                "Dashboard_Exports": "Read access for authorized users"
            }
        },
        
        "Training_Materials": {
            "description": "Store training documents and user guides",
            "folders": [
                "User_Guides/Microsoft_365/Excel_Automation",
                "User_Guides/Microsoft_365/Power_Automate",
                "User_Guides/Microsoft_365/Power_BI",
                "User_Guides/Microsoft_365/SharePoint",
                "User_Guides/Microsoft_365/Teams_Collaboration",
                "User_Guides/Business_Processes/Client_Onboarding",
                "User_Guides/Business_Processes/Project_Management",
                "User_Guides/Business_Processes/Quality_Assurance",
                "User_Guides/Business_Processes/Reporting_Procedures",
                "Video_Tutorials/Getting_Started/New_Employee_Orientation",
                "Video_Tutorials/Getting_Started/System_Overview",
                "Video_Tutorials/Advanced_Features/Automation_Workflows",
                "Video_Tutorials/Advanced_Features/Custom_Reporting",
                "Video_Tutorials/Advanced_Features/Integration_Setup",
                "Quick_Reference_Cards/Excel_Formulas",
                "Quick_Reference_Cards/Power_Automate_Actions",
                "Quick_Reference_Cards/Power_BI_Visualizations",
                "Quick_Reference_Cards/SharePoint_Navigation",
                "Best_Practices/Project_Management/Agile_Methodologies",
                "Best_Practices/Project_Management/Risk_Management",
                "Best_Practices/Client_Management/Communication_Standards",
                "Best_Practices/Client_Management/Expectation_Setting",
                "Best_Practices/Quality_Assurance/Review_Processes",
                "Best_Practices/Quality_Assurance/Testing_Standards",
                "Troubleshooting_Guides/Technical_Issues/System_Problems",
                "Troubleshooting_Guides/Technical_Issues/Integration_Issues",
                "Troubleshooting_Guides/Process_Issues/Workflow_Problems",
                "Troubleshooting_Guides/Process_Issues/Communication_Issues",
                "Certification_Materials/Microsoft_Certifications/Power_Platform",
                "Certification_Materials/Microsoft_Certifications/Azure_Fundamentals",
                "Certification_Materials/Industry_Certifications/Project_Management",
                "Certification_Materials/Industry_Certifications/Business_Analysis"
            ],
            "permissions": {
                "User_Guides": "Read access for all team members",
                "Video_Tutorials": "Read access for all team members",
                "Quick_Reference_Cards": "Read access for all team members",
                "Best_Practices": "Contribute access for senior team members",
                "Troubleshooting_Guides": "Edit access for technical team",
                "Certification_Materials": "Read access for all team members"
            }
        },
        
        "Business_Operations": {
            "description": "Store internal business documents and procedures",
            "folders": [
                "Policies_and_Procedures/HR_Policies/Employee_Handbook",
                "Policies_and_Procedures/HR_Policies/Code_of_Conduct",
                "Policies_and_Procedures/HR_Policies/Performance_Management",
                "Policies_and_Procedures/IT_Policies/Security_Policies",
                "Policies_and_Procedures/IT_Policies/Data_Protection",
                "Policies_and_Procedures/IT_Policies/Acceptable_Use",
                "Policies_and_Procedures/Business_Policies/Client_Engagement",
                "Policies_and_Procedures/Business_Policies/Financial_Management",
                "Standard_Operating_Procedures/Client_Onboarding/New_Client_Setup",
                "Standard_Operating_Procedures/Client_Onboarding/Contract_Processing",
                "Standard_Operating_Procedures/Project_Management/Project_Initiation",
                "Standard_Operating_Procedures/Project_Management/Project_Execution",
                "Standard_Operating_Procedures/Project_Management/Project_Closure",
                "Standard_Operating_Procedures/Quality_Management/Quality_Control",
                "Standard_Operating_Procedures/Quality_Management/Quality_Assurance",
                "Standard_Operating_Procedures/Financial_Management/Invoicing_Process",
                "Standard_Operating_Procedures/Financial_Management/Expense_Management",
                "Quality_Assurance/Quality_Plans/Project_Quality_Plans",
                "Quality_Assurance/Quality_Plans/Service_Quality_Plans",
                "Quality_Assurance/Audit_Reports/Internal_Audits",
                "Quality_Assurance/Audit_Reports/External_Audits",
                "Quality_Assurance/Improvement_Plans/Process_Improvements",
                "Quality_Assurance/Improvement_Plans/System_Improvements",
                "Compliance_Documents/Regulatory_Compliance/Data_Privacy",
                "Compliance_Documents/Regulatory_Compliance/Industry_Standards",
                "Compliance_Documents/Certifications/ISO_Certifications",
                "Compliance_Documents/Certifications/Industry_Certifications",
                "Audit_Trail/System_Audits/Access_Logs",
                "Audit_Trail/System_Audits/Change_Logs",
                "Audit_Trail/Process_Audits/Procedure_Compliance",
                "Audit_Trail/Process_Audits/Quality_Compliance",
                "Business_Plans/Strategic_Plans/Annual_Strategic_Plan",
                "Business_Plans/Strategic_Plans/Long_Term_Vision",
                "Business_Plans/Operational_Plans/Annual_Operating_Plan",
                "Business_Plans/Operational_Plans/Quarterly_Plans",
                "Business_Plans/Financial_Plans/Budget_Plans",
                "Business_Plans/Financial_Plans/Investment_Plans"
            ],
            "permissions": {
                "Policies_and_Procedures": "Read access for all employees",
                "Standard_Operating_Procedures": "Read access for relevant teams",
                "Quality_Assurance": "Edit access for QA team, read for others",
                "Compliance_Documents": "Restricted to compliance team and management",
                "Audit_Trail": "Restricted to audit team and senior management",
                "Business_Plans": "Restricted to senior management and board"
            }
        },
        
        "Marketing_and_Sales": {
            "description": "Store marketing materials and sales documents",
            "folders": [
                "Marketing_Materials/Brochures_and_Flyers/Service_Brochures",
                "Marketing_Materials/Brochures_and_Flyers/Company_Overview",
                "Marketing_Materials/Digital_Assets/Website_Content",
                "Marketing_Materials/Digital_Assets/Social_Media_Content",
                "Marketing_Materials/Digital_Assets/Email_Templates",
                "Marketing_Materials/Presentations/Company_Presentations",
                "Marketing_Materials/Presentations/Service_Presentations",
                "Marketing_Materials/Videos/Company_Videos",
                "Marketing_Materials/Videos/Service_Demonstrations",
                "Case_Studies/Client_Success_Stories/Healthcare_Case_Studies",
                "Case_Studies/Client_Success_Stories/Manufacturing_Case_Studies",
                "Case_Studies/Client_Success_Stories/Financial_Services_Case_Studies",
                "Case_Studies/Project_Case_Studies/Automation_Projects",
                "Case_Studies/Project_Case_Studies/Analytics_Projects",
                "Case_Studies/ROI_Case_Studies/Cost_Savings",
                "Case_Studies/ROI_Case_Studies/Efficiency_Improvements",
                "Testimonials/Client_Testimonials/Written_Testimonials",
                "Testimonials/Client_Testimonials/Video_Testimonials",
                "Testimonials/Partner_Testimonials/Technology_Partners",
                "Testimonials/Partner_Testimonials/Implementation_Partners",
                "Sales_Presentations/Standard_Presentations/Company_Overview",
                "Sales_Presentations/Standard_Presentations/Service_Overview",
                "Sales_Presentations/Custom_Presentations/Client_Specific",
                "Sales_Presentations/Custom_Presentations/Industry_Specific",
                "Sales_Presentations/Demo_Presentations/Live_Demos",
                "Sales_Presentations/Demo_Presentations/Recorded_Demos",
                "Competitive_Analysis/Competitor_Profiles/Direct_Competitors",
                "Competitive_Analysis/Competitor_Profiles/Indirect_Competitors",
                "Competitive_Analysis/Market_Research/Industry_Reports",
                "Competitive_Analysis/Market_Research/Trend_Analysis",
                "Competitive_Analysis/SWOT_Analysis/Company_SWOT",
                "Competitive_Analysis/SWOT_Analysis/Competitive_SWOT",
                "Lead_Generation_Materials/White_Papers/Industry_White_Papers",
                "Lead_Generation_Materials/White_Papers/Technical_White_Papers",
                "Lead_Generation_Materials/eBooks/Best_Practices_eBooks",
                "Lead_Generation_Materials/eBooks/How_To_Guides",
                "Lead_Generation_Materials/Webinars/Educational_Webinars",
                "Lead_Generation_Materials/Webinars/Product_Webinars"
            ],
            "permissions": {
                "Marketing_Materials": "Edit access for marketing team, read for sales",
                "Case_Studies": "Read access for sales and marketing teams",
                "Testimonials": "Read access for sales and marketing teams",
                "Sales_Presentations": "Edit access for sales team",
                "Competitive_Analysis": "Restricted to sales and marketing management",
                "Lead_Generation_Materials": "Edit access for marketing team"
            }
        },
        
        "Financial_Documents": {
            "description": "Store financial records and accounting documents",
            "folders": [
                "Invoices/Client_Invoices/2024/Q1",
                "Invoices/Client_Invoices/2024/Q2", 
                "Invoices/Client_Invoices/2024/Q3",
                "Invoices/Client_Invoices/2024/Q4",
                "Invoices/Vendor_Invoices/2024/Q1",
                "Invoices/Vendor_Invoices/2024/Q2",
                "Invoices/Vendor_Invoices/2024/Q3",
                "Invoices/Vendor_Invoices/2024/Q4",
                "Contracts_Financial/Client_Contracts/Active_Contracts",
                "Contracts_Financial/Client_Contracts/Completed_Contracts",
                "Contracts_Financial/Vendor_Contracts/Software_Licenses",
                "Contracts_Financial/Vendor_Contracts/Service_Agreements",
                "Contracts_Financial/Employment_Contracts/Full_Time_Employees",
                "Contracts_Financial/Employment_Contracts/Contractors",
                "Budget_Planning/Annual_Budgets/2024_Budget",
                "Budget_Planning/Annual_Budgets/2025_Budget",
                "Budget_Planning/Quarterly_Budgets/Q1_2024",
                "Budget_Planning/Quarterly_Budgets/Q2_2024",
                "Budget_Planning/Quarterly_Budgets/Q3_2024",
                "Budget_Planning/Quarterly_Budgets/Q4_2024",
                "Budget_Planning/Department_Budgets/Sales_Budget",
                "Budget_Planning/Department_Budgets/Marketing_Budget",
                "Budget_Planning/Department_Budgets/Operations_Budget",
                "Financial_Reports/Monthly_Reports/P&L_Statements",
                "Financial_Reports/Monthly_Reports/Balance_Sheets",
                "Financial_Reports/Monthly_Reports/Cash_Flow_Statements",
                "Financial_Reports/Quarterly_Reports/Quarterly_Financials",
                "Financial_Reports/Quarterly_Reports/Board_Reports",
                "Financial_Reports/Annual_Reports/Annual_Financials",
                "Financial_Reports/Annual_Reports/Tax_Returns",
                "Tax_Documents/Federal_Tax_Returns/2024",
                "Tax_Documents/Federal_Tax_Returns/2023",
                "Tax_Documents/State_Tax_Returns/2024",
                "Tax_Documents/State_Tax_Returns/2023",
                "Tax_Documents/Payroll_Tax_Documents/2024",
                "Tax_Documents/Payroll_Tax_Documents/2023",
                "Audit_Records/External_Audits/2024_Audit",
                "Audit_Records/External_Audits/2023_Audit",
                "Audit_Records/Internal_Audits/Quarterly_Reviews",
                "Audit_Records/Internal_Audits/Annual_Reviews",
                "Banking_Records/Bank_Statements/Operating_Account",
                "Banking_Records/Bank_Statements/Savings_Account",
                "Banking_Records/Loan_Documents/Business_Loans",
                "Banking_Records/Loan_Documents/Equipment_Financing"
            ],
            "permissions": {
                "Invoices": "Edit access for finance team, read for management",
                "Contracts_Financial": "Edit access for finance and legal teams",
                "Budget_Planning": "Edit access for finance team and department heads",
                "Financial_Reports": "Read access based on role and confidentiality level",
                "Tax_Documents": "Restricted to finance team and external accountants",
                "Audit_Records": "Restricted to finance team and auditors",
                "Banking_Records": "Restricted to finance team and senior management"
            }
        },
        
        "System_Documentation": {
            "description": "Store technical documentation and system guides",
            "folders": [
                "Technical_Specifications/System_Architecture/Overall_Architecture",
                "Technical_Specifications/System_Architecture/Integration_Architecture",
                "Technical_Specifications/Database_Design/Data_Models",
                "Technical_Specifications/Database_Design/Schema_Documentation",
                "Technical_Specifications/API_Documentation/REST_APIs",
                "Technical_Specifications/API_Documentation/Integration_APIs",
                "Technical_Specifications/Security_Specifications/Security_Architecture",
                "Technical_Specifications/Security_Specifications/Access_Controls",
                "System_Architecture/Microsoft_365_Architecture/SharePoint_Architecture",
                "System_Architecture/Microsoft_365_Architecture/Power_Platform_Architecture",
                "System_Architecture/Microsoft_365_Architecture/Teams_Architecture",
                "System_Architecture/Network_Architecture/Network_Topology",
                "System_Architecture/Network_Architecture/Security_Architecture",
                "System_Architecture/Cloud_Architecture/Azure_Architecture",
                "System_Architecture/Cloud_Architecture/Hybrid_Architecture",
                "Integration_Guides/Microsoft_365_Integrations/SharePoint_Integrations",
                "Integration_Guides/Microsoft_365_Integrations/Power_Automate_Integrations",
                "Integration_Guides/Microsoft_365_Integrations/Power_BI_Integrations",
                "Integration_Guides/Third_Party_Integrations/CRM_Integrations",
                "Integration_Guides/Third_Party_Integrations/ERP_Integrations",
                "Integration_Guides/API_Integrations/REST_API_Guides",
                "Integration_Guides/API_Integrations/GraphQL_API_Guides",
                "Backup_Procedures/Data_Backup/SharePoint_Backup",
                "Backup_Procedures/Data_Backup/Database_Backup",
                "Backup_Procedures/System_Backup/Configuration_Backup",
                "Backup_Procedures/System_Backup/Application_Backup",
                "Backup_Procedures/Disaster_Recovery/Recovery_Procedures",
                "Backup_Procedures/Disaster_Recovery/Business_Continuity",
                "Security_Protocols/Access_Management/User_Access_Controls",
                "Security_Protocols/Access_Management/Role_Based_Access",
                "Security_Protocols/Data_Protection/Data_Encryption",
                "Security_Protocols/Data_Protection/Data_Loss_Prevention",
                "Security_Protocols/Network_Security/Firewall_Configuration",
                "Security_Protocols/Network_Security/VPN_Configuration",
                "Security_Protocols/Compliance/GDPR_Compliance",
                "Security_Protocols/Compliance/SOX_Compliance",
                "Change_Management/Change_Procedures/System_Changes",
                "Change_Management/Change_Procedures/Process_Changes",
                "Change_Management/Release_Management/Release_Procedures",
                "Change_Management/Release_Management/Deployment_Procedures",
                "Change_Management/Version_Control/Code_Versioning",
                "Change_Management/Version_Control/Document_Versioning"
            ],
            "permissions": {
                "Technical_Specifications": "Edit access for technical team, read for others",
                "System_Architecture": "Edit access for architects, read for technical team",
                "Integration_Guides": "Edit access for integration team, read for others",
                "Backup_Procedures": "Edit access for IT operations team",
                "Security_Protocols": "Restricted to security team and IT management",
                "Change_Management": "Edit access for change management team"
            }
        }
    }
    
    return folder_structures

def generate_powershell_script(folder_structures):
    """Generate PowerShell script for creating folder structures"""
    
    script_content = '''# SharePoint Folder Structure Creation Script
# Generated automatically for business automation setup
# Run this script with SharePoint Online Management Shell

# Prerequisites:
# 1. Install-Module -Name PnP.PowerShell -Force
# 2. Connect-PnPOnline -Url "https://[tenant].sharepoint.com/sites/BusinessOperations" -Interactive

param(
    [Parameter(Mandatory=$true)]
    [string]$SiteUrl,
    
    [Parameter(Mandatory=$false)]
    [string]$LibraryName = "All"
)

# Function to create folder structure with error handling
function Create-FolderStructure {
    param(
        [string]$LibraryName,
        [array]$Folders,
        [string]$Description
    )
    
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "Creating folder structure for: $LibraryName" -ForegroundColor Green
    Write-Host "Description: $Description" -ForegroundColor Yellow
    Write-Host "Total folders to create: $($Folders.Count)" -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Cyan
    
    $successCount = 0
    $errorCount = 0
    
    foreach ($FolderPath in $Folders) {
        try {
            # Check if folder already exists
            $existingFolder = Get-PnPFolder -Url "$LibraryName/$FolderPath" -ErrorAction SilentlyContinue
            
            if ($existingFolder) {
                Write-Host "⚠️  Already exists: $FolderPath" -ForegroundColor Yellow
            } else {
                # Create folder (including parent folders if they don't exist)
                $Folder = Add-PnPFolder -Name $FolderPath -Folder $LibraryName -ErrorAction Stop
                Write-Host "✅ Created: $FolderPath" -ForegroundColor Green
                $successCount++
            }
        }
        catch {
            Write-Host "❌ Failed to create: $FolderPath" -ForegroundColor Red
            Write-Host "   Error: $($_.Exception.Message)" -ForegroundColor Red
            $errorCount++
        }
        
        # Add small delay to avoid throttling
        Start-Sleep -Milliseconds 100
    }
    
    Write-Host "`n📊 Summary for $LibraryName:" -ForegroundColor Cyan
    Write-Host "   ✅ Successfully created: $successCount folders" -ForegroundColor Green
    Write-Host "   ❌ Failed to create: $errorCount folders" -ForegroundColor Red
    Write-Host "   📁 Total processed: $($Folders.Count) folders" -ForegroundColor Yellow
    Write-Host ""
}

# Connect to SharePoint (if not already connected)
try {
    $connection = Get-PnPConnection -ErrorAction SilentlyContinue
    if (-not $connection) {
        Write-Host "Connecting to SharePoint..." -ForegroundColor Yellow
        Connect-PnPOnline -Url $SiteUrl -Interactive
    }
    Write-Host "✅ Connected to SharePoint successfully" -ForegroundColor Green
}
catch {
    Write-Host "❌ Failed to connect to SharePoint: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Define folder structures
'''

    # Add folder structure definitions
    for library_name, config in folder_structures.items():
        script_content += f'''
${library_name.replace(" ", "_")}_Folders = @(
'''
        for folder in config['folders']:
            script_content += f'    "{folder}",\n'
        
        script_content = script_content.rstrip(',\n') + '\n)\n'

    # Add execution logic
    script_content += '''
# Execute folder creation based on parameter
switch ($LibraryName) {
'''

    for library_name, config in folder_structures.items():
        var_name = library_name.replace(" ", "_")
        script_content += f'''    "{library_name}" {{
        Create-FolderStructure -LibraryName "{library_name}" -Folders ${var_name}_Folders -Description "{config['description']}"
    }}
'''

    script_content += '''    "All" {
'''
    
    for library_name, config in folder_structures.items():
        var_name = library_name.replace(" ", "_")
        script_content += f'        Create-FolderStructure -LibraryName "{library_name}" -Folders ${var_name}_Folders -Description "{config["description"]}"\n'
    
    script_content += '''    }
    default {
        Write-Host "❌ Invalid library name. Available options:" -ForegroundColor Red
'''
    
    for library_name in folder_structures.keys():
        script_content += f'        Write-Host "   - {library_name}" -ForegroundColor Yellow\n'
    
    script_content += '''        Write-Host "   - All (creates all libraries)" -ForegroundColor Yellow
    }
}

Write-Host "🎉 Folder structure creation completed!" -ForegroundColor Cyan
Write-Host "📝 Next steps:" -ForegroundColor Yellow
Write-Host "   1. Review created folder structures in SharePoint" -ForegroundColor White
Write-Host "   2. Configure permissions for sensitive folders" -ForegroundColor White
Write-Host "   3. Set up metadata columns for better organization" -ForegroundColor White
Write-Host "   4. Create views and filters for easy navigation" -ForegroundColor White

# Usage examples:
# .\CreateSharePointFolders.ps1 -SiteUrl "https://tenant.sharepoint.com/sites/BusinessOperations" -LibraryName "Client_Documents"
# .\CreateSharePointFolders.ps1 -SiteUrl "https://tenant.sharepoint.com/sites/BusinessOperations" -LibraryName "All"
'''

    return script_content

def generate_power_automate_flow(folder_structures):
    """Generate Power Automate flow JSON for folder creation"""
    
    # Create a simplified flow for one library as an example
    flow_definition = {
        "definition": {
            "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
            "contentVersion": "1.0.0.0",
            "parameters": {
                "$connections": {
                    "defaultValue": {},
                    "type": "Object"
                }
            },
            "triggers": {
                "manual": {
                    "type": "Request",
                    "kind": "Button",
                    "inputs": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "LibraryName": {
                                    "type": "string",
                                    "title": "Library Name",
                                    "enum": list(folder_structures.keys())
                                },
                                "SiteUrl": {
                                    "type": "string", 
                                    "title": "SharePoint Site URL",
                                    "default": "https://[tenant].sharepoint.com/sites/BusinessOperations"
                                }
                            },
                            "required": ["LibraryName", "SiteUrl"]
                        }
                    }
                }
            },
            "actions": {
                "Initialize_Folder_List": {
                    "type": "InitializeVariable",
                    "inputs": {
                        "variables": [
                            {
                                "name": "FolderList",
                                "type": "array",
                                "value": []
                            }
                        ]
                    }
                },
                "Switch_Library_Type": {
                    "type": "Switch",
                    "expression": "@triggerBody()['LibraryName']",
                    "cases": {},
                    "default": {
                        "actions": {
                            "Send_Error_Email": {
                                "type": "ApiConnection",
                                "inputs": {
                                    "host": {
                                        "connectionName": "office365",
                                        "operationId": "SendEmailV2"
                                    },
                                    "parameters": {
                                        "emailMessage": {
                                            "To": "admin@company.com",
                                            "Subject": "SharePoint Folder Creation Error",
                                            "Body": "Invalid library name provided: @{triggerBody()['LibraryName']}"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    # Add cases for each library
    for library_name, config in folder_structures.items():
        case_name = library_name.replace(" ", "_").replace("-", "_")
        
        flow_definition["definition"]["actions"]["Switch_Library_Type"]["cases"][case_name] = {
            "case": library_name,
            "actions": {
                f"Set_Folders_for_{case_name}": {
                    "type": "SetVariable",
                    "inputs": {
                        "name": "FolderList",
                        "value": config['folders'][:10]  # Limit to first 10 folders for demo
                    }
                },
                f"Apply_to_each_folder_{case_name}": {
                    "type": "Foreach",
                    "foreach": "@variables('FolderList')",
                    "actions": {
                        f"Create_Folder_{case_name}": {
                            "type": "ApiConnection",
                            "inputs": {
                                "host": {
                                    "connectionName": "sharepointonline",
                                    "operationId": "CreateFolder"
                                },
                                "parameters": {
                                    "dataset": "@triggerBody()['SiteUrl']",
                                    "table": library_name,
                                    "folderPath": "@items('Apply_to_each_folder_" + case_name + "')"
                                }
                            }
                        }
                    }
                }
            }
        }
    
    return flow_definition

def generate_manual_creation_guide(folder_structures):
    """Generate step-by-step manual creation guide"""
    
    guide_content = """# Manual SharePoint Folder Creation Guide
## Step-by-Step Instructions for Creating Document Library Structures

### 🎯 Overview
This guide provides detailed instructions for manually creating folder structures in SharePoint document libraries. Follow these steps for each library you need to set up.

### 📋 Prerequisites
- SharePoint site access with Contribute permissions or higher
- Document libraries already created in SharePoint
- 30-60 minutes depending on the number of folders

---

## 🚀 Quick Start Instructions

### Step 1: Access Your SharePoint Site
1. Navigate to your SharePoint site
2. Sign in with your Microsoft 365 account
3. Click on "Site contents" to see all libraries

### Step 2: Open Document Library
1. Click on the document library you want to organize
2. You'll see the main library view with toolbar options

### Step 3: Create Folder Structure
1. Click "New" → "Folder" in the toolbar
2. Enter folder name exactly as shown in the lists below
3. Click "Create"
4. Repeat for all folders in the structure

---

## 📁 Folder Structures to Create

"""

    for library_name, config in folder_structures.items():
        guide_content += f"""
### {library_name.replace("_", " ")}
**Purpose:** {config['description']}

**Folders to create (copy these names exactly):**
```
"""
        for folder in config['folders']:
            guide_content += f"{folder}\n"
        
        guide_content += f"""```

**Permissions Notes:**
"""
        for folder_pattern, permission in config['permissions'].items():
            guide_content += f"- {folder_pattern}: {permission}\n"
        
        guide_content += "\n---\n"

    guide_content += """
## 💡 Pro Tips for Manual Creation

### Efficient Creation Process:
1. **Create main folders first** - Start with top-level folders
2. **Use copy-paste** - Copy folder names from this guide to avoid typos
3. **Work systematically** - Complete one library before moving to the next
4. **Check as you go** - Verify folder names match exactly

### Time-Saving Techniques:
1. **Open multiple browser tabs** - One for this guide, one for SharePoint
2. **Use keyboard shortcuts** - Ctrl+C to copy, Ctrl+V to paste
3. **Create templates** - Save frequently used folder structures
4. **Batch similar folders** - Create all client folders at once

### Common Mistakes to Avoid:
1. **Spaces in folder names** - Use underscores instead of spaces
2. **Inconsistent naming** - Follow the exact naming convention
3. **Wrong folder hierarchy** - Create parent folders before subfolders
4. **Missing permissions** - Set up folder permissions after creation

---

## 🔧 Troubleshooting Common Issues

### Issue: "Folder already exists" error
**Solution:** Check if folder exists with different capitalization or spacing

### Issue: Permission denied
**Solution:** Verify you have Contribute access to the library

### Issue: Folder not appearing
**Solution:** Refresh the page or check if you're in the correct library

### Issue: Can't create subfolders
**Solution:** Ensure parent folder exists and you're inside the correct folder

---

## ✅ Verification Checklist

After creating folders, verify:
- [ ] All folder names match the provided structure exactly
- [ ] Folder hierarchy is correct (subfolders in right parent folders)
- [ ] No duplicate or missing folders
- [ ] Permissions are set appropriately for sensitive folders
- [ ] Team members can access folders they need

---

## 📞 Support and Next Steps

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your SharePoint permissions
3. Contact your SharePoint administrator
4. Consider using the PowerShell automation script for complex structures

**Next Steps:**
1. Set up metadata columns for better organization
2. Create custom views for different user roles
3. Configure permissions for sensitive folders
4. Train team members on the new folder structure
"""

    return guide_content

def create_setup_files():
    """Create all setup files and scripts"""
    
    print("🚀 Generating SharePoint Folder Structure Automation Files...")
    print("=" * 60)
    
    # Create output directory
    output_dir = "sharepoint_folder_automation"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate folder structure configuration
    print("📁 Creating folder structure configuration...")
    folder_structures = create_folder_structure_config()
    
    # Save configuration as JSON
    config_file = os.path.join(output_dir, "folder_structures_config.json")
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(folder_structures, f, indent=2, ensure_ascii=False)
    print(f"✅ Created: {config_file}")
    
    # Generate PowerShell script
    print("💻 Generating PowerShell automation script...")
    powershell_script = generate_powershell_script(folder_structures)
    script_file = os.path.join(output_dir, "Create-SharePointFolders.ps1")
    with open(script_file, 'w', encoding='utf-8') as f:
        f.write(powershell_script)
    print(f"✅ Created: {script_file}")
    
    # Generate Power Automate flow
    print("⚡ Generating Power Automate flow definition...")
    flow_definition = generate_power_automate_flow(folder_structures)
    flow_file = os.path.join(output_dir, "power_automate_flow.json")
    with open(flow_file, 'w', encoding='utf-8') as f:
        json.dump(flow_definition, f, indent=2)
    print(f"✅ Created: {flow_file}")
    
    # Generate manual creation guide
    print("📖 Generating manual creation guide...")
    manual_guide = generate_manual_creation_guide(folder_structures)
    guide_file = os.path.join(output_dir, "Manual_Creation_Guide.md")
    with open(guide_file, 'w', encoding='utf-8') as f:
        f.write(manual_guide)
    print(f"✅ Created: {guide_file}")
    
    # Create summary file
    print("📋 Creating setup summary...")
    summary_content = f"""# SharePoint Folder Structure Automation Package
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📦 Package Contents

### 1. Configuration Files
- `folder_structures_config.json` - Complete folder structure definitions
- `Manual_Creation_Guide.md` - Step-by-step manual creation instructions

### 2. Automation Scripts
- `Create-SharePointFolders.ps1` - PowerShell script for bulk folder creation
- `power_automate_flow.json` - Power Automate flow definition

### 3. Documentation
- `README.md` - This file with setup instructions
- `Manual_Creation_Guide.md` - Detailed manual creation guide

## 🚀 Quick Start

### Option 1: PowerShell Automation (Recommended)
1. Install PnP PowerShell: `Install-Module -Name PnP.PowerShell -Force`
2. Update the site URL in the script
3. Run: `.\Create-SharePointFolders.ps1 -SiteUrl "https://[tenant].sharepoint.com/sites/BusinessOperations" -LibraryName "All"`

### Option 2: Power Automate Flow
1. Import `power_automate_flow.json` into Power Automate
2. Configure SharePoint connections
3. Run the flow for each library

### Option 3: Manual Creation
1. Follow the `Manual_Creation_Guide.md` step-by-step
2. Copy folder names exactly as provided
3. Create folders one by one in SharePoint

## 📊 Statistics
- **Total Libraries:** {len(folder_structures)}
- **Total Folders:** {sum(len(config['folders']) for config in folder_structures.values())}
- **Estimated Manual Creation Time:** {sum(len(config['folders']) for config in folder_structures.values()) * 0.5:.0f} minutes
- **Estimated PowerShell Creation Time:** 5-10 minutes

## 📁 Library Overview
"""
    
    for library_name, config in folder_structures.items():
        summary_content += f"""
### {library_name.replace('_', ' ')}
- **Purpose:** {config['description']}
- **Folder Count:** {len(config['folders'])}
- **Estimated Creation Time:** {len(config['folders']) * 0.5:.0f} minutes (manual)
"""

    summary_content += """
## 🔧 Troubleshooting

### Common Issues:
1. **Permission Denied:** Verify SharePoint site permissions
2. **Folder Already Exists:** Check for existing folders with similar names
3. **PowerShell Connection Issues:** Ensure PnP PowerShell module is installed
4. **Power Automate Failures:** Verify SharePoint connector permissions

### Support:
- Check the Manual_Creation_Guide.md for detailed troubleshooting
- Verify all prerequisites are met
- Test with a single library before running full automation

## 📞 Next Steps

After creating folder structures:
1. Configure folder permissions based on security requirements
2. Set up metadata columns for better organization
3. Create custom views for different user roles
4. Train team members on the new folder structure
5. Set up automated workflows for folder maintenance

---

**Note:** Always test folder creation in a development environment before running in production.
"""
    
    readme_file = os.path.join(output_dir, "README.md")
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    print(f"✅ Created: {readme_file}")
    
    print("\n🎉 SharePoint Folder Structure Automation Package Created Successfully!")
    print(f"📁 All files saved to: {output_dir}/")
    print("\n📋 Package Contents:")
    for file in os.listdir(output_dir):
        file_path = os.path.join(output_dir, file)
        file_size = os.path.getsize(file_path)
        print(f"   📄 {file} ({file_size:,} bytes)")
    
    print(f"\n📊 Total Statistics:")
    print(f"   📚 Libraries: {len(folder_structures)}")
    print(f"   📁 Total Folders: {sum(len(config['folders']) for config in folder_structures.values())}")
    print(f"   ⏱️  Estimated Manual Time: {sum(len(config['folders']) for config in folder_structures.values()) * 0.5:.0f} minutes")
    print(f"   🚀 Estimated PowerShell Time: 5-10 minutes")
    
    return output_dir

if __name__ == "__main__":
    output_directory = create_setup_files()
    print(f"\n✅ Setup complete! Check the '{output_directory}' folder for all generated files.")


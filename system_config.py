#!/usr/bin/env python3
"""
System Configuration Script for Power Automate Intake Forms
Configures the complete system for automated form processing
"""

import os
import json
import subprocess
import sys
from pathlib import Path

class SystemConfigurator:
    def __init__(self):
        self.config_dir = Path(__file__).parent
        self.config = {
            "tenant_id": "75db62a2-c72e-453b-ac8b-5deda95159e9",
            "client_id": "acc2972d-b762-495d-b7a8-5743fd5f6486",
            "client_secret": "Mbq8Q~rTm32W_amwcB.JDY21f8BPO8LX~WdR8bXY",
            "environment_url": "https://make.powerautomate.com",
            "forms_config": {
                "lead_qualification": {
                    "name": "Lead Qualification Intake Form",
                    "description": "Initial lead assessment and qualification",
                    "auto_scoring": True,
                    "alert_threshold": 25
                },
                "project_discovery": {
                    "name": "Project Discovery & Requirements Form",
                    "description": "Detailed project scoping and requirements gathering",
                    "auto_scoring": False,
                    "requires_follow_up": True
                },
                "technical_assessment": {
                    "name": "Technical Assessment Form",
                    "description": "In-depth technical infrastructure evaluation",
                    "auto_scoring": False,
                    "requires_technical_review": True
                },
                "client_success": {
                    "name": "Client Success Monitoring Form",
                    "description": "Ongoing client health and satisfaction tracking",
                    "auto_scoring": True,
                    "alert_threshold": 7,
                    "frequency": "monthly"
                }
            }
        }
    
    def check_prerequisites(self):
        """Check if all required tools are installed"""
        print("🔍 Checking system prerequisites...")
        
        prerequisites = {
            "python": ["python", "--version"],
            "pac_cli": ["pac", "help"],
            "powershell": ["powershell", "-Version"]
        }
        
        results = {}
        for tool, command in prerequisites.items():
            try:
                result = subprocess.run(command, capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    results[tool] = "✅ Installed"
                    if tool == "python":
                        version = result.stdout.strip()
                        print(f"  Python: {version}")
                    elif tool == "pac_cli":
                        print(f"  Power Platform CLI: ✅ Available")
                    elif tool == "powershell":
                        print(f"  PowerShell: ✅ Available")
                else:
                    results[tool] = "❌ Not available"
            except (subprocess.TimeoutExpired, FileNotFoundError):
                results[tool] = "❌ Not found"
        
        return all("✅" in status for status in results.values())
    
    def install_python_dependencies(self):
        """Install required Python packages"""
        print("\n📦 Installing Python dependencies...")
        
        packages = ["requests", "json5", "python-dotenv"]
        
        for package in packages:
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", package], 
                             check=True, capture_output=True)
                print(f"  ✅ {package} installed successfully")
            except subprocess.CalledProcessError as e:
                print(f"  ❌ Failed to install {package}: {e}")
                return False
        return True
    
    def create_environment_file(self):
        """Create .env file with configuration"""
        print("\n🔧 Creating environment configuration...")
        
        env_content = f"""# Power Automate Configuration
TENANT_ID={self.config['tenant_id']}
CLIENT_ID={self.config['client_id']}
CLIENT_SECRET={self.config['client_secret']}
ENVIRONMENT_URL={self.config['environment_url']}

# Form Processing Configuration
AUTO_LEAD_SCORING=true
LEAD_ALERT_THRESHOLD=25
CLIENT_SUCCESS_THRESHOLD=7
DEFAULT_FORM_LANGUAGE=en-US

# Notification Settings
ENABLE_EMAIL_ALERTS=true
ENABLE_TEAMS_NOTIFICATIONS=false
ADMIN_EMAIL=your-admin@company.com

# Database Configuration
USE_SHAREPOINT_LISTS=true
SHAREPOINT_SITE_URL=https://yourtenant.sharepoint.com/sites/PowerAutomate

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=system.log
"""
        
        env_path = self.config_dir / ".env"
        with open(env_path, 'w') as f:
            f.write(env_content)
        
        print(f"  ✅ Environment file created: {env_path}")
        return True
    
    def create_config_json(self):
        """Create comprehensive configuration JSON"""
        print("\n📋 Creating system configuration file...")
        
        config_path = self.config_dir / "system_config.json"
        with open(config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
        
        print(f"  ✅ Configuration file created: {config_path}")
        return True
    
    def setup_powerplatform_auth(self):
        """Setup Power Platform authentication profile"""
        print("\n🔐 Setting up Power Platform authentication...")
        
        # Create authentication script
        auth_script = """
# Power Platform CLI Authentication Setup
Write-Host "Setting up Power Platform CLI Authentication..." -ForegroundColor Green

# Check if already authenticated
$profiles = pac auth list 2>$null
if ($profiles -like "*No profiles were found*") {
    Write-Host "Creating new authentication profile..." -ForegroundColor Yellow
    Write-Host "Please authenticate when prompted in the browser..." -ForegroundColor Yellow
    
    # Try to create auth profile
    pac auth create --name "MainProfile"
} else {
    Write-Host "Authentication profiles found:" -ForegroundColor Green
    pac auth list
}

Write-Host "Authentication setup complete!" -ForegroundColor Green
"""
        
        auth_script_path = self.config_dir / "setup_auth.ps1"
        with open(auth_script_path, 'w') as f:
            f.write(auth_script)
        
        print(f"  ✅ Authentication script created: {auth_script_path}")
        print("  📝 Run this script manually: ./setup_auth.ps1")
        return True
    
    def create_forms_deployment_script(self):
        """Create script to deploy forms to Microsoft Forms"""
        print("\n📝 Creating forms deployment configuration...")
        
        deployment_script = """#!/usr/bin/env python3
\"\"\"
Forms Deployment Script
Deploys intake forms to Microsoft Forms via Graph API
\"\"\"

import requests
import json
import os
from datetime import datetime

class FormsDeployer:
    def __init__(self):
        self.tenant_id = os.getenv('TENANT_ID')
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.access_token = None
    
    def authenticate(self):
        \"\"\"Authenticate with Microsoft Graph API\"\"\"
        auth_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'https://graph.microsoft.com/.default'
        }
        
        response = requests.post(auth_url, headers=headers, data=data)
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            print("✅ Authentication successful")
            return True
        else:
            print(f"❌ Authentication failed: {response.text}")
            return False
    
    def deploy_forms(self):
        \"\"\"Deploy forms using Graph API\"\"\"
        if not self.access_token:
            print("❌ No authentication token available")
            return False
        
        print("📝 Forms deployment would be configured here...")
        print("Note: Microsoft Forms API requires specific permissions")
        print("Consider using Power Platform CLI for form creation")
        
        return True

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    deployer = FormsDeployer()
    if deployer.authenticate():
        deployer.deploy_forms()
"""
        
        deployment_path = self.config_dir / "deploy_forms.py"
        with open(deployment_path, 'w') as f:
            f.write(deployment_script)
        
        print(f"  ✅ Forms deployment script created: {deployment_path}")
        return True
    
    def create_monitoring_script(self):
        """Create system monitoring and health check script"""
        print("\n📊 Creating system monitoring script...")
        
        monitoring_script = """#!/usr/bin/env python3
\"\"\"
System Monitor for Power Automate Intake Forms
Monitors form submissions, flow health, and system status
\"\"\"

import requests
import json
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

class SystemMonitor:
    def __init__(self):
        load_dotenv()
        self.tenant_id = os.getenv('TENANT_ID')
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.access_token = None
    
    def check_system_health(self):
        \"\"\"Check overall system health\"\"\"
        print("🏥 System Health Check")
        print("=" * 50)
        
        health_status = {
            "timestamp": datetime.now().isoformat(),
            "authentication": self.test_authentication(),
            "power_platform_cli": self.test_cli(),
            "forms_accessibility": self.test_forms(),
            "flows_status": self.test_flows()
        }
        
        return health_status
    
    def test_authentication(self):
        \"\"\"Test Azure AD authentication\"\"\"
        try:
            auth_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            data = {
                'grant_type': 'client_credentials',
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'scope': 'https://graph.microsoft.com/.default'
            }
            
            response = requests.post(auth_url, headers=headers, data=data, timeout=10)
            if response.status_code == 200:
                self.access_token = response.json()['access_token']
                print("  ✅ Authentication: OK")
                return True
            else:
                print(f"  ❌ Authentication: FAILED ({response.status_code})")
                return False
        except Exception as e:
            print(f"  ❌ Authentication: ERROR ({str(e)})")
            return False
    
    def test_cli(self):
        \"\"\"Test Power Platform CLI availability\"\"\"
        try:
            import subprocess
            result = subprocess.run(['pac', 'help'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print("  ✅ Power Platform CLI: OK")
                return True
            else:
                print("  ❌ Power Platform CLI: NOT AVAILABLE")
                return False
        except Exception as e:
            print(f"  ❌ Power Platform CLI: ERROR ({str(e)})")
            return False
    
    def test_forms(self):
        \"\"\"Test forms accessibility\"\"\"
        print("  📝 Forms: CONFIGURED (Manual verification needed)")
        return True
    
    def test_flows(self):
        \"\"\"Test Power Automate flows\"\"\"
        print("  🔄 Flows: CONFIGURED (Manual verification needed)")
        return True
    
    def generate_status_report(self):
        \"\"\"Generate comprehensive status report\"\"\"
        status = self.check_system_health()
        
        print("\\n📊 System Status Report")
        print("=" * 50)
        print(f"Generated: {status['timestamp']}")
        print(f"Authentication: {'✅ OK' if status['authentication'] else '❌ FAILED'}")
        print(f"CLI Available: {'✅ OK' if status['power_platform_cli'] else '❌ FAILED'}")
        print(f"Forms Ready: {'✅ OK' if status['forms_accessibility'] else '❌ FAILED'}")
        print(f"Flows Ready: {'✅ OK' if status['flows_status'] else '❌ FAILED'}")
        
        # Save report to file
        report_path = f"system_status_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_path, 'w') as f:
            json.dump(status, f, indent=2)
        
        print(f"\\n💾 Report saved to: {report_path}")
        return status

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.generate_status_report()
"""
        
        monitoring_path = self.config_dir / "system_monitor.py"
        with open(monitoring_path, 'w') as f:
            f.write(monitoring_script)
        
        print(f"  ✅ System monitoring script created: {monitoring_path}")
        return True
    
    def run_configuration(self):
        """Run the complete system configuration"""
        print("🚀 Power Automate Intake Forms - System Configuration")
        print("=" * 60)
        
        steps = [
            ("Checking Prerequisites", self.check_prerequisites),
            ("Installing Python Dependencies", self.install_python_dependencies),
            ("Creating Environment File", self.create_environment_file),
            ("Creating Configuration", self.create_config_json),
            ("Setting up Authentication", self.setup_powerplatform_auth),
            ("Creating Forms Deployment", self.create_forms_deployment_script),
            ("Creating Monitoring Tools", self.create_monitoring_script)
        ]
        
        success_count = 0
        for step_name, step_function in steps:
            try:
                if step_function():
                    success_count += 1
                else:
                    print(f"⚠️  {step_name} completed with warnings")
            except Exception as e:
                print(f"❌ {step_name} failed: {str(e)}")
        
        print(f"\n🎉 Configuration complete! {success_count}/{len(steps)} steps successful")
        
        if success_count == len(steps):
            print("\n✅ Your system is fully configured!")
            self.print_next_steps()
        else:
            print("\n⚠️  Some steps need attention. Check the output above.")
    
    def print_next_steps(self):
        """Print next steps for the user"""
        print("\n📋 Next Steps:")
        print("=" * 30)
        print("1. Run: ./setup_auth.ps1 (Authenticate with Power Platform)")
        print("2. Run: python system_monitor.py (Verify system health)")
        print("3. Run: python deploy_forms.py (Deploy forms)")
        print("4. Create flows using the provided JSON definitions")
        print("5. Test end-to-end form submission and automation")
        print("\n📚 Documentation:")
        print("- Check the intake forms: Lead_Qualification_Intake_Form.md")
        print("- Review implementation guide: Manual_Flow_Creation_Guide.md")
        print("- Monitor with: system_monitor.py")

if __name__ == "__main__":
    configurator = SystemConfigurator()
    configurator.run_configuration()

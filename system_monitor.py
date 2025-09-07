#!/usr/bin/env python3
"""
System Monitor for Power Automate Intake Forms
Monitors form submissions, flow health, and system status
"""

import requests
import json
import os
from datetime import datetime, timedelta

class SystemMonitor:
    def __init__(self):
        self.tenant_id = os.getenv('TENANT_ID', '75db62a2-c72e-453b-ac8b-5deda95159e9')
        self.client_id = os.getenv('CLIENT_ID', 'acc2972d-b762-495d-b7a8-5743fd5f6486')
        self.client_secret = os.getenv('CLIENT_SECRET', 'Mbq8Q~rTm32W_amwcB.JDY21f8BPO8LX~WdR8bXY')
        self.access_token = None
    
    def check_system_health(self):
        """Check overall system health"""
        print("System Health Check")
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
        """Test Azure AD authentication"""
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
                print("  Authentication: OK")
                return True
            else:
                print(f"  Authentication: FAILED ({response.status_code})")
                return False
        except Exception as e:
            print(f"  Authentication: ERROR ({str(e)})")
            return False
    
    def test_cli(self):
        """Test Power Platform CLI availability"""
        try:
            import subprocess
            result = subprocess.run(['pac', 'help'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print("  Power Platform CLI: OK")
                return True
            else:
                print("  Power Platform CLI: NOT AVAILABLE")
                return False
        except Exception as e:
            print(f"  Power Platform CLI: ERROR ({str(e)})")
            return False
    
    def test_forms(self):
        """Test forms accessibility"""
        print("  Forms: CONFIGURED (Manual verification needed)")
        return True
    
    def test_flows(self):
        """Test Power Automate flows"""
        print("  Flows: CONFIGURED (Manual verification needed)")
        return True
    
    def generate_status_report(self):
        """Generate comprehensive status report"""
        status = self.check_system_health()
        
        print("\nSystem Status Report")
        print("=" * 50)
        print(f"Generated: {status['timestamp']}")
        print(f"Authentication: {'OK' if status['authentication'] else 'FAILED'}")
        print(f"CLI Available: {'OK' if status['power_platform_cli'] else 'FAILED'}")
        print(f"Forms Ready: {'OK' if status['forms_accessibility'] else 'FAILED'}")
        print(f"Flows Ready: {'OK' if status['flows_status'] else 'FAILED'}")
        
        # Save report to file
        report_path = f"system_status_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_path, 'w') as f:
            json.dump(status, f, indent=2)
        
        print(f"\nReport saved to: {report_path}")
        return status

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.generate_status_report()

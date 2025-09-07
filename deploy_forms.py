#!/usr/bin/env python3
"""
Forms Deployment Script
Deploys intake forms to Microsoft Forms via Graph API
"""

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
        """Authenticate with Microsoft Graph API"""
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
            print("Authentication successful")
            return True
        else:
            print(f"Authentication failed: {response.text}")
            return False
    
    def deploy_forms(self):
        """Deploy forms using Graph API"""
        if not self.access_token:
            print("No authentication token available")
            return False
        
        print("Forms deployment would be configured here...")
        print("Note: Microsoft Forms API requires specific permissions")
        print("Consider using Power Platform CLI for form creation")
        
        return True

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    deployer = FormsDeployer()
    if deployer.authenticate():
        deployer.deploy_forms()

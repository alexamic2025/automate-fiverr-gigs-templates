# 🚀 Quick Deployment Commands
## PowerShell Commands That Work with Spaces in Folder Names

---

## ✅ **Fixed Commands for Your Environment**

### 🎯 **Easy Deployment (Recommended)**
```powershell
# Run the interactive deployment (choose option 1 for browser setup)
& ".\deploy_to_power_platform.ps1"
```

### 📊 **System Status Check**
```powershell
# Check system health
& "python" "system_monitor.py"

# Check authentication
pac auth list

# List environments  
pac env list
```

### 🔧 **Alternative Deployment Methods**
```powershell
# SharePoint and Power Automate setup
& ".\deploy_sharepoint_powerautomate.ps1"

# System configuration check
& ".\system_status.ps1"
```

---

## 🌐 **Browser-Based Setup (Fastest Method)**

**Run this command and select Option 1:**
```powershell
& ".\deploy_to_power_platform.ps1"
```

**Then type: `1` and press Enter**

This will automatically open:
- ✅ SharePoint for list creation
- ✅ Power Automate for flow import
- ✅ Microsoft Forms for form creation  
- ✅ Setup guide documentation

---

## 📋 **Manual URL Access** (If browser setup doesn't work)

### SharePoint Lists
```
https://actlearningsystems.sharepoint.com/sites/PowerAutomate/_layouts/15/viewlsts.aspx
```

### Power Automate Flows
```
https://make.powerautomate.com/environments/75db62a2-c72e-453b-ac8b-5deda95159e9/flows
```

### Microsoft Forms
```
https://forms.microsoft.com
```

---

## 🛠️ **Troubleshooting Path Issues**

### Problem: Spaces in Folder Path
❌ **This won't work:**
```powershell
C:\Users\alexa\Automate Fiverr Gigs with Uploaded Templates\deploy_to_power_platform.ps1
```

✅ **These will work:**
```powershell
# Option 1: Use quotes and call operator
& ".\deploy_to_power_platform.ps1"

# Option 2: Use quotes with full path
& "C:\Users\alexa\Automate Fiverr Gigs with Uploaded Templates\deploy_to_power_platform.ps1"

# Option 3: Use dot-slash notation (if in the directory)
.\deploy_to_power_platform.ps1
```

---

## ⚡ **Quick Start - 3 Commands**

```powershell
# 1. Run deployment script
& ".\deploy_to_power_platform.ps1"

# 2. Select option 1 when prompted

# 3. Follow the opened browser tabs to set up your forms
```

**Total time: 15-30 minutes for complete setup!**

---

## 📁 **What You Have Ready**

### ✅ **SharePoint Templates**
- `lead_qualification_sharepoint_list.json`
- `project_discovery_sharepoint_list.json`  
- `technical_assessment_sharepoint_list.json`
- `client_success_sharepoint_list.json`

### ✅ **Power Automate Flows**
- `Lead_Qualification_Flow.json` - Automated lead scoring
- `Project_Discovery_Flow.json` - Project processing
- `Technical_Assessment_Flow.json` - Technical risk alerts  
- `Client_Success_Flow.json` - Client health monitoring

### ✅ **Intake Forms**
- `Lead_Qualification_Intake_Form.md`
- `Project_Discovery_Requirements_Form.md`
- `Technical_Assessment_Form.md`
- `Client_Success_Monitoring_Form.md`

### ✅ **Solution Package**
- `IntakeFormsSolution/` folder with all components ready for import

---

## 🎯 **Next Action**

**Copy and paste this command:**
```powershell
& ".\deploy_to_power_platform.ps1"
```

**Select `1` for browser setup - it's the easiest way to get everything configured!**

# Power Platform Direct Deployment Script
# Automated deployment to your ACT Learning Systems environment

param(
    [string]$EnvironmentUrl = "https://actlearningsystemsdefault.crm.dynamics.com/",
    [string]$SharePointSite = "https://actlearningsystems.sharepoint.com"
)

Write-Host "=" * 70 -ForegroundColor Cyan
Write-Host "🚀 POWER PLATFORM DIRECT DEPLOYMENT" -ForegroundColor Green
Write-Host "   Intake Forms → SharePoint → Power Automate" -ForegroundColor White
Write-Host "=" * 70 -ForegroundColor Cyan

Write-Host "`n🎯 Deployment Target:" -ForegroundColor Yellow
Write-Host "  Environment: ACT Learning Systems (default)" -ForegroundColor White
Write-Host "  URL: $EnvironmentUrl" -ForegroundColor White
Write-Host "  SharePoint: $SharePointSite" -ForegroundColor White

# Check authentication
Write-Host "`n🔐 Checking Authentication..." -ForegroundColor Cyan
$authStatus = pac auth list
if ($authStatus -like "*Hello@alldataflow.com*") {
    Write-Host "  ✅ Authenticated as: Hello@alldataflow.com" -ForegroundColor Green
} else {
    Write-Host "  ❌ Authentication required. Run: pac auth create" -ForegroundColor Red
    exit 1
}

# Check available flows
Write-Host "`n🔍 Scanning Available Flow Templates..." -ForegroundColor Cyan
$flowFiles = Get-ChildItem -Path "." -Filter "*Flow.json"
foreach ($file in $flowFiles) {
    Write-Host "  📄 Found: $($file.Name)" -ForegroundColor Green
}

# Check SharePoint templates
Write-Host "`n📋 Scanning SharePoint List Templates..." -ForegroundColor Cyan  
$listFiles = Get-ChildItem -Path "." -Filter "*sharepoint_list.json"
foreach ($file in $listFiles) {
    Write-Host "  📊 Found: $($file.Name)" -ForegroundColor Green
}

# Direct deployment options
Write-Host "`n🚀 Deployment Options:" -ForegroundColor Yellow

Write-Host "`n1️⃣  OPTION 1: Quick Browser Setup (Recommended)" -ForegroundColor Cyan
Write-Host "   Opens all necessary portals for manual setup:" -ForegroundColor White
Write-Host "   • SharePoint List creation" -ForegroundColor Gray
Write-Host "   • Power Automate flow import" -ForegroundColor Gray  
Write-Host "   • Microsoft Forms creation" -ForegroundColor Gray

Write-Host "`n2️⃣  OPTION 2: PowerShell Commands" -ForegroundColor Cyan
Write-Host "   Provides copy-paste commands for terminal execution" -ForegroundColor White

Write-Host "`n3️⃣  OPTION 3: Generate Import Package" -ForegroundColor Cyan
Write-Host "   Creates solution package for direct import" -ForegroundColor White

$choice = Read-Host "`nSelect deployment option (1, 2, or 3)"

switch ($choice) {
    "1" {
        Write-Host "`n🌐 Opening Browser-Based Setup..." -ForegroundColor Green
        
        # Open SharePoint for list creation
        Write-Host "  📊 Opening SharePoint for list creation..." -ForegroundColor Cyan
        Start-Process "https://actlearningsystems.sharepoint.com/sites/PowerAutomate/_layouts/15/viewlsts.aspx"
        Start-Sleep 2
        
        # Open Power Automate for flow creation
        Write-Host "  🔄 Opening Power Automate for flow import..." -ForegroundColor Cyan
        Start-Process "https://make.powerautomate.com/environments/75db62a2-c72e-453b-ac8b-5deda95159e9/flows"
        Start-Sleep 2
        
        # Open Microsoft Forms
        Write-Host "  📝 Opening Microsoft Forms..." -ForegroundColor Cyan
        Start-Process "https://forms.microsoft.com"
        Start-Sleep 2
        
        # Open setup guide
        Write-Host "  📖 Opening setup guide..." -ForegroundColor Cyan
        Start-Process "SharePoint_PowerAutomate_Setup_Guide.md"
        
        Write-Host "`n✅ All portals opened! Follow the setup guide for step-by-step instructions." -ForegroundColor Green
    }
    
    "2" {
        Write-Host "`n💻 PowerShell Commands for Direct Deployment:" -ForegroundColor Green
        
        Write-Host "`n📊 SharePoint List Creation Commands:" -ForegroundColor Cyan
        Write-Host "# Install PnP PowerShell (if not installed)" -ForegroundColor Gray
        Write-Host "Install-Module -Name PnP.PowerShell -Force" -ForegroundColor White
        Write-Host "`n# Connect to SharePoint" -ForegroundColor Gray
        Write-Host "Connect-PnPOnline -Url 'https://actlearningsystems.sharepoint.com/sites/PowerAutomate' -Interactive" -ForegroundColor White
        
        Write-Host "`n# Create Lead Qualification List" -ForegroundColor Gray
        Write-Host "New-PnPList -Title 'Lead Qualification Intake' -Template GenericList" -ForegroundColor White
        
        Write-Host "`n🔄 Power Automate Commands:" -ForegroundColor Cyan
        Write-Host "# List current flows" -ForegroundColor Gray
        Write-Host "pac flow list" -ForegroundColor White
        
        Write-Host "`n# Note: Flow import requires manual process via portal" -ForegroundColor Gray
        Write-Host "# Use the browser option for easier flow deployment" -ForegroundColor Yellow
    }
    
    "3" {
        Write-Host "`n📦 Generating Solution Package..." -ForegroundColor Green
        
        # Create solution structure
        $solutionDir = "IntakeFormsSolution"
        if (Test-Path $solutionDir) {
            Remove-Item $solutionDir -Recurse -Force
        }
        New-Item -ItemType Directory -Path $solutionDir -Force | Out-Null
        
        # Copy flow definitions
        Copy-Item "*Flow.json" -Destination $solutionDir -ErrorAction SilentlyContinue
        
        # Copy SharePoint templates  
        Copy-Item "*sharepoint_list.json" -Destination $solutionDir -ErrorAction SilentlyContinue
        
        # Copy intake forms
        Copy-Item "*Form.md" -Destination $solutionDir -ErrorAction SilentlyContinue
        
        # Create solution metadata
        $solutionXml = @"
<?xml version="1.0" encoding="utf-8"?>
<ImportExportXml version="9.1.0.643" SolutionPackageVersion="9.1" languagecode="1033" generatedBy="PowerPlatformCLI">
  <SolutionManifest>
    <UniqueName>IntakeFormsSolution</UniqueName>
    <LocalizedNames>
      <LocalizedName description="Intake Forms Automation Solution" languagecode="1033" />
    </LocalizedNames>
    <Descriptions>
      <Description description="Comprehensive intake forms with SharePoint lists and Power Automate flows" languagecode="1033" />
    </Descriptions>
    <Version>1.0.0.0</Version>
    <Managed>0</Managed>
    <Publisher>
      <UniqueName>ACTLearningSystems</UniqueName>
      <LocalizedNames>
        <LocalizedName description="ACT Learning Systems" languagecode="1033" />
      </LocalizedNames>
    </Publisher>
  </SolutionManifest>
</ImportExportXml>
"@
        
        $solutionXml | Out-File -FilePath "$solutionDir/solution.xml" -Encoding UTF8
        
        Write-Host "  ✅ Solution package created: $solutionDir" -ForegroundColor Green
        Write-Host "  📁 Contains:" -ForegroundColor Cyan
        Get-ChildItem $solutionDir | ForEach-Object {
            Write-Host "    • $($_.Name)" -ForegroundColor White
        }
    }
    
    default {
        Write-Host "`n❌ Invalid option. Please run the script again and select 1, 2, or 3." -ForegroundColor Red
        exit 1
    }
}

Write-Host "`n📋 Next Steps Summary:" -ForegroundColor Yellow
Write-Host "1. ✅ All templates and flows are ready" -ForegroundColor Green
Write-Host "2. 🔄 SharePoint lists need to be created" -ForegroundColor White
Write-Host "3. 📝 Microsoft Forms need to be built" -ForegroundColor White  
Write-Host "4. 🔗 Power Automate flows need to be imported" -ForegroundColor White
Write-Host "5. 🧪 End-to-end testing required" -ForegroundColor White

Write-Host "`n📚 Documentation Available:" -ForegroundColor Cyan
Write-Host "  • SharePoint_PowerAutomate_Setup_Guide.md - Complete setup instructions" -ForegroundColor White
Write-Host "  • QUICK_REFERENCE.md - Quick commands and overview" -ForegroundColor White
Write-Host "  • Lead_Qualification_Intake_Form.md - Start here for first form" -ForegroundColor White

Write-Host "`n🎉 Your intake forms are ready for deployment!" -ForegroundColor Green
Write-Host "Estimated deployment time: 2-3 hours for complete setup" -ForegroundColor Yellow
Write-Host "`nRecommendation: Start with Option 1 (Browser Setup) for easiest deployment" -ForegroundColor Cyan

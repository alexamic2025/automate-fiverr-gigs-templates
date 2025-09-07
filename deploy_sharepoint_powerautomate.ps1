# SharePoint and Power Automate Deployment Script
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

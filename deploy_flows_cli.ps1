# Power Platform CLI Flow Deployment Script
# This script uses the Power Platform CLI to deploy flows

Write-Host "=== Power Platform CLI Flow Deployment ===" -ForegroundColor Cyan
Write-Host ""

# Configuration
$tenantId = "75db62a2-c72e-453b-ac8b-5deda95159e9"
$environmentUrl = "https://org75db62a2c72e453bac8b5deda95159e9.crm.dynamics.com"  # Update with your actual environment URL
$environmentName = "Default-75db62a2-c72e-453b-ac8b-5deda95159e9"

# Flow definition files
$flowFiles = @(
    "flow_lead_qualification.json",
    "flow_client_success.json", 
    "flow_reporting_pipeline.json"
)

Write-Host "Step 1: Installing Power Platform CLI..." -ForegroundColor Yellow
try {
    # Check if CLI is already installed
    $cliVersion = pac --version 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Power Platform CLI is already installed: $cliVersion" -ForegroundColor Green
    } else {
        Write-Host "Power Platform CLI not found. Please install it manually from:" -ForegroundColor Yellow
        Write-Host "https://docs.microsoft.com/en-us/power-platform/developer/cli/introduction" -ForegroundColor White
        Write-Host ""
        Write-Host "Alternative installation methods:" -ForegroundColor Yellow
        Write-Host "1. Download MSI: https://aka.ms/PowerPlatformCLI" -ForegroundColor White
        Write-Host "2. Use npm: npm install -g @microsoft/powerplatform-cli" -ForegroundColor White
        Write-Host "3. Use dotnet: dotnet tool install --global Microsoft.PowerApps.CLI.Tool" -ForegroundColor White
        Write-Host ""
        Read-Host "Press Enter after installing the CLI to continue"
    }
}
catch {
    Write-Host "❌ Error checking CLI installation: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "Step 2: Authenticating with Power Platform..." -ForegroundColor Yellow
try {
    # Authenticate using device code flow
    pac auth create --url $environmentUrl --name "FlowDeployment"
    Write-Host "✅ Authentication successful" -ForegroundColor Green
}
catch {
    Write-Host "❌ Authentication failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Manual authentication steps:" -ForegroundColor Yellow
    Write-Host "1. Run: pac auth create --url $environmentUrl" -ForegroundColor White
    Write-Host "2. Follow the device code authentication flow" -ForegroundColor White
    exit 1
}

Write-Host ""
Write-Host "Step 3: Deploying flows..." -ForegroundColor Yellow

$successfulDeployments = @()
$failedDeployments = @()

foreach ($flowFile in $flowFiles) {
    Write-Host "Deploying flow from $flowFile..." -ForegroundColor White
    
    try {
        # Create flow using CLI
        $result = pac flow create --definition-file $flowFile --environment $environmentName
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Successfully deployed $flowFile" -ForegroundColor Green
            $successfulDeployments += $flowFile
        } else {
            Write-Host "❌ Failed to deploy $flowFile" -ForegroundColor Red
            $failedDeployments += $flowFile
        }
    }
    catch {
        Write-Host "❌ Error deploying $flowFile : $($_.Exception.Message)" -ForegroundColor Red
        $failedDeployments += $flowFile
    }
    
    Write-Host ""
    Start-Sleep -Seconds 2
}

Write-Host "=== Deployment Summary ===" -ForegroundColor Cyan
Write-Host "✅ Successful deployments: $($successfulDeployments.Count)" -ForegroundColor Green
foreach ($success in $successfulDeployments) {
    Write-Host "  - $success" -ForegroundColor White
}

Write-Host "❌ Failed deployments: $($failedDeployments.Count)" -ForegroundColor Red
foreach ($failed in $failedDeployments) {
    Write-Host "  - $failed" -ForegroundColor White
}

Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Go to Power Automate portal: https://flow.microsoft.com" -ForegroundColor White
Write-Host "2. Verify the flows were created successfully" -ForegroundColor White
Write-Host "3. Configure connections for each flow as needed" -ForegroundColor White
Write-Host "4. Test each flow to ensure proper functionality" -ForegroundColor White
Write-Host ""

# Alternative manual deployment instructions
Write-Host "=== Manual Deployment Instructions ===" -ForegroundColor Cyan
Write-Host "If CLI deployment fails, you can manually import the flows:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Go to https://flow.microsoft.com" -ForegroundColor White
Write-Host "2. Click 'My flows' > 'Import' > 'Import Package (.zip)'" -ForegroundColor White
Write-Host "3. Or create new flows using the JSON definitions as reference" -ForegroundColor White
Write-Host ""
Write-Host "Flow definition files created:" -ForegroundColor Yellow
foreach ($file in $flowFiles) {
    Write-Host "  - $file" -ForegroundColor White
}

Write-Host ""
Read-Host "Press Enter to exit"

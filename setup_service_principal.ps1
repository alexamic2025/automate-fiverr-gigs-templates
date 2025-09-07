# PowerShell Script to Setup Service Principal for Power Automate
# Run this script as an administrator with Global Admin or Power Platform Admin rights

Write-Host "=== Power Platform Service Principal Setup ===" -ForegroundColor Cyan
Write-Host ""

# Step 1: Install required PowerShell modules
Write-Host "Step 1: Installing required PowerShell modules..." -ForegroundColor Yellow
try {
    Install-Module -Name Microsoft.PowerApps.Administration.PowerShell -Force -AllowClobber -Scope CurrentUser
    Install-Module -Name Microsoft.PowerApps.PowerShell -Force -AllowClobber -Scope CurrentUser
    Write-Host "✅ Modules installed successfully" -ForegroundColor Green
}
catch {
    Write-Host "❌ Error installing modules: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Step 2: Configuration variables
Write-Host "Step 2: Setting up configuration..." -ForegroundColor Yellow
$tenantId = "75db62a2-c72e-453b-ac8b-5deda95159e9"
$clientId = "acc2972d-b762-495d-b7a8-5743fd5f6486" 
$environmentId = "Default-75db62a2-c72e-453b-ac8b-5deda95159e9"

Write-Host "Configuration:" -ForegroundColor Cyan
Write-Host "  Tenant ID: $tenantId" -ForegroundColor White
Write-Host "  Client ID: $clientId" -ForegroundColor White
Write-Host "  Environment ID: $environmentId" -ForegroundColor White
Write-Host ""

# Step 3: Connect to Power Platform
Write-Host "Step 3: Connecting to Power Platform..." -ForegroundColor Yellow
try {
    Add-PowerAppsAccount
    Write-Host "✅ Connected to Power Platform successfully" -ForegroundColor Green
}
catch {
    Write-Host "❌ Error connecting to Power Platform: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Step 4: Get the service principal
Write-Host "Step 4: Getting service principal information..." -ForegroundColor Yellow
try {
    # Connect to Azure AD first
    Connect-AzAccount -TenantId $tenantId
    
    # Get the service principal
    $servicePrincipal = Get-AzADServicePrincipal -ApplicationId $clientId -ErrorAction SilentlyContinue
    
    if ($null -eq $servicePrincipal) {
        Write-Host "❌ Service principal not found. Please ensure the app registration exists." -ForegroundColor Red
        exit 1
    }
    
    Write-Host "✅ Service Principal found:" -ForegroundColor Green
    Write-Host "  Display Name: $($servicePrincipal.DisplayName)" -ForegroundColor White
    Write-Host "  Object ID: $($servicePrincipal.Id)" -ForegroundColor White
}
catch {
    Write-Host "❌ Error getting service principal: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Step 5: Add service principal as Environment Admin
Write-Host "Step 5: Adding service principal as Environment Admin..." -ForegroundColor Yellow
try {
    New-AdminPowerAppRoleAssignment -EnvironmentName $environmentId -RoleName "Environment Admin" -PrincipalType "ServicePrincipal" -PrincipalObjectId $servicePrincipal.Id
    Write-Host "✅ Service principal added as Environment Admin" -ForegroundColor Green
}
catch {
    Write-Host "❌ Error adding Environment Admin role: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Trying Environment Maker role..." -ForegroundColor Yellow
    
    try {
        New-AdminPowerAppRoleAssignment -EnvironmentName $environmentId -RoleName "Environment Maker" -PrincipalType "ServicePrincipal" -PrincipalObjectId $servicePrincipal.Id
        Write-Host "✅ Service principal added as Environment Maker" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ Alternative method also failed: $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host ""

# Step 6: Add Flow service permissions
Write-Host "Step 6: Adding Flow service permissions..." -ForegroundColor Yellow
try {
    # Add the service principal to Flow service
    New-AdminFlowUserRoleAssignment -EnvironmentName $environmentId -UserId $servicePrincipal.Id -RoleName "CanEdit"
    Write-Host "✅ Flow edit permissions added" -ForegroundColor Green
}
catch {
    Write-Host "⚠️  Flow permissions may need manual configuration: $($_.Exception.Message)" -ForegroundColor Yellow
}

Write-Host ""

# Step 7: Verify role assignments
Write-Host "Step 7: Verifying role assignments..." -ForegroundColor Yellow
try {
    $roleAssignments = Get-AdminPowerAppRoleAssignment -EnvironmentName $environmentId
    $myAssignment = $roleAssignments | Where-Object { $_.PrincipalObjectId -eq $servicePrincipal.Id }
    
    if ($null -ne $myAssignment) {
        Write-Host "✅ Role assignment verified:" -ForegroundColor Green
        foreach ($assignment in $myAssignment) {
            Write-Host "  Role: $($assignment.RoleName)" -ForegroundColor White
        }
    } else {
        Write-Host "⚠️  Role assignment not found in verification" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "❌ Error verifying role assignment: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "=== Setup Complete ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Wait 5-10 minutes for permissions to propagate" -ForegroundColor White
Write-Host "2. Run your Python script: python automated_flow_creator.py" -ForegroundColor White
Write-Host "3. Manual verification in Power Platform Admin Center:" -ForegroundColor White
Write-Host "   https://admin.powerplatform.microsoft.com/" -ForegroundColor White
Write-Host ""
Read-Host "Press Enter to exit"

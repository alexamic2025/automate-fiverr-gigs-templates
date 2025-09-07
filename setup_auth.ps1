
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

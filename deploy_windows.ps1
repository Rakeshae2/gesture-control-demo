# Deployment helper for Windows Server (run via RDP as the interactive user)
# - Creates .venv, installs dependencies from requirements.txt
# - Opens firewall port 8000
# - Starts Uvicorn in a new PowerShell window (keeps the desktop session active)
# NOTE: gesture.py requires an interactive desktop session with camera access. Run this script while connected via RDP
#       and keep the RDP session active (or configure an autologin interactive session). Running as a Windows Service
#       will likely prevent pyautogui and camera access.

$projectDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Write-Host "Project directory: $projectDir"

# 1) Check Python availability
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Error "Python is not found in PATH. Please install Python 3.8+ and ensure 'python' is on PATH, then re-run this script."
    exit 1
}

# 2) Create virtual environment if missing
$venvPath = Join-Path $projectDir ".venv"
if (-not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment at $venvPath ..."
    python -m venv "$venvPath"
} else {
    Write-Host "Virtual environment already exists at $venvPath"
}

# 3) Activate venv and install requirements
$activateScript = Join-Path $venvPath "Scripts\Activate.ps1"
if (-not (Test-Path $activateScript)) {
    Write-Error "Activation script not found at $activateScript"
    exit 1
}

Write-Host "Installing Python dependencies from requirements.txt..."
& "$activateScript"; pip install --upgrade pip
& "$activateScript"; pip install -r (Join-Path $projectDir "requirements.txt")

# 4) Open firewall port for Uvicorn (8000)
try {
    New-NetFirewallRule -DisplayName "Gesture App Uvicorn" -Direction Inbound -LocalPort 8000 -Protocol TCP -Action Allow -ErrorAction Stop | Out-Null
    Write-Host "Firewall rule added for port 8000"
} catch {
    Write-Warning "Could not add firewall rule (it might already exist or require elevation)."
}

# 5) Start the app in a new PowerShell window so GUI/camera access works under the interactive session
$uvicornCmd = "& '$activateScript'; python -m uvicorn app:app --host 0.0.0.0 --port 8000"
Write-Host "Starting Uvicorn in a new interactive PowerShell window..."
Start-Process powershell -ArgumentList '-NoExit','-Command', $uvicornCmd -WorkingDirectory $projectDir

Write-Host "Deployment script finished. If the app did not start, check the PowerShell window for errors."
Write-Host "Important notes:" -ForegroundColor Yellow
Write-Host " - Keep the RDP session active (do not log off) if you need gesture.py (pyautogui/camera) to work." -ForegroundColor Yellow
Write-Host " - To run the app automatically on user logon, consider creating a scheduled task that runs this Start-Process command at logon under the interactive user." -ForegroundColor Yellow
Write-Host " - If you prefer running the app as a background service, NSSM can wrap the Python command, BUT services usually won't have access to the interactive desktop/camera." -ForegroundColor Yellow

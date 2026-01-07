# Setup Script untuk Aplikasi Deteksi Korosi
# Jalankan script ini untuk setup awal

Write-Host "🚀 Setup Aplikasi Deteksi Korosi" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Green
Write-Host ""

# Check Python
Write-Host "📌 Checking Python installation..." -ForegroundColor Cyan
try {
    $pythonVersion = python --version
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python tidak ditemukan. Install Python terlebih dahulu." -ForegroundColor Red
    exit 1
}

Write-Host ""

# Install dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Cyan
try {
    pip install -r requirements.txt
    Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ Error installing dependencies" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Check model file
Write-Host "🔍 Checking model file..." -ForegroundColor Cyan
if (Test-Path "saved_model.keras") {
    Write-Host "✅ Model file found: saved_model.keras" -ForegroundColor Green
} else {
    Write-Host "⚠️  Model file not found!" -ForegroundColor Yellow
    Write-Host "   Please copy your trained model file (saved_model.keras) to this directory" -ForegroundColor Yellow
}

Write-Host ""

# Check API Key
Write-Host "🔑 Checking Gemini API Key..." -ForegroundColor Cyan
if ($env:GEMINI_API_KEY) {
    $keyLength = $env:GEMINI_API_KEY.Length
    Write-Host "✅ API Key found (length: $keyLength)" -ForegroundColor Green
} else {
    Write-Host "⚠️  GEMINI_API_KEY not set!" -ForegroundColor Yellow
    Write-Host "   Set it using: `$env:GEMINI_API_KEY='your-api-key-here'" -ForegroundColor Yellow
    Write-Host ""
    $response = Read-Host "Do you want to set it now? (y/n)"
    if ($response -eq "y" -or $response -eq "Y") {
        $apiKey = Read-Host "Enter your Gemini API Key"
        $env:GEMINI_API_KEY = $apiKey
        Write-Host "✅ API Key set for this session" -ForegroundColor Green
        Write-Host "   Note: To make it permanent, add it to your system environment variables" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "=================================" -ForegroundColor Green
Write-Host "✅ Setup completed!" -ForegroundColor Green
Write-Host ""
Write-Host "To run the application:" -ForegroundColor Cyan
Write-Host "  streamlit run app.py" -ForegroundColor White
Write-Host ""
Write-Host "To set API key permanently:" -ForegroundColor Cyan
Write-Host "  [Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'your-key', 'User')" -ForegroundColor White
Write-Host ""

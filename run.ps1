# Quick Start Script
# Jalankan aplikasi Streamlit dengan mudah

Write-Host "🚀 Starting Corrosion Detection App..." -ForegroundColor Green

# Check if API key is set
if (-not $env:GEMINI_API_KEY) {
    Write-Host "⚠️  Warning: GEMINI_API_KEY not set" -ForegroundColor Yellow
    Write-Host "   AI analysis will not work without it" -ForegroundColor Yellow
    Write-Host ""
}

# Run Streamlit
streamlit run app.py

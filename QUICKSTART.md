# 🚀 Quick Start Guide

## Langkah 1: Copy Model File

Copy file model Anda yang sudah dilatih (`saved_model.keras`) ke folder ini:

```
corrosion/
├── saved_model.keras  ← Taruh model di sini
├── app.py
└── ...
```

**Lokasi model dari file Anda:**
- Dari Google Colab: `/content/drive/MyDrive/.../saved_model.keras`
- Copy ke: `c:\Users\90003686\ROBBY_DATA\Repos\corrosion\saved_model.keras`

## Langkah 2: Install Dependencies

Buka PowerShell di folder ini dan jalankan:

```powershell
pip install -r requirements.txt
```

## Langkah 3: Setup Gemini API Key

### Dapatkan API Key:
1. Kunjungi: https://makersuite.google.com/app/apikey
2. Login dengan Google Account
3. Klik "Create API Key"
4. Copy API key yang dihasilkan

### Set API Key di PowerShell:

```powershell
$env:GEMINI_API_KEY="paste-your-api-key-here"
```

**Untuk set permanent:**
```powershell
[Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'your-key-here', 'User')
```

## Langkah 4: Jalankan Aplikasi

```powershell
streamlit run app.py
```

Atau gunakan script helper:
```powershell
.\run.ps1
```

## 🧪 Test Setup (Optional)

Sebelum menjalankan app, test dulu:

```powershell
python test_setup.py
```

Ini akan check:
- ✅ Semua library terinstall
- ✅ Model file ada
- ✅ API key ter-set
- ✅ Model bisa di-load

## 📝 Checklist

Sebelum menjalankan app, pastikan:

- [ ] File `saved_model.keras` sudah ada di folder ini
- [ ] Dependencies sudah terinstall (`pip install -r requirements.txt`)
- [ ] Gemini API Key sudah di-set (`$env:GEMINI_API_KEY`)
- [ ] Test setup berhasil (`python test_setup.py`)

## 🎯 Cara Menggunakan Aplikasi

1. **Upload Gambar**: Klik "Browse files" dan pilih gambar logam
2. **Lihat Hasil**: Model akan otomatis mendeteksi korosi
3. **Analisis AI**: Klik "Lakukan Analisis Mendalam" untuk laporan detail
4. **Download**: Simpan laporan dengan klik "Download Laporan Analisis"

## ⚠️ Troubleshooting

### "Model tidak dapat dimuat"
**Solusi:**
- Pastikan file `saved_model.keras` ada
- Check path-nya benar
- Coba load manual di Python untuk cek error detail

### "API Key tidak ditemukan"
**Solusi:**
```powershell
# Check apakah sudah di-set
echo $env:GEMINI_API_KEY

# Jika belum, set lagi
$env:GEMINI_API_KEY="your-key"
```

### "Import Error"
**Solusi:**
```powershell
# Reinstall dependencies
pip uninstall -y -r requirements.txt
pip install -r requirements.txt
```

### "Port sudah digunakan"
**Solusi:**
```powershell
# Gunakan port lain
streamlit run app.py --server.port 8502
```

## 📚 File Structure

```
corrosion/
├── app.py                    # Aplikasi utama (local)
├── app_cloud.py             # Versi untuk cloud deployment
├── saved_model.keras        # Model terlatih (TIDAK di-commit ke git)
├── requirements.txt         # Python dependencies
├── README.md               # Dokumentasi lengkap
├── DEPLOYMENT.md           # Panduan deployment
├── QUICKSTART.md           # File ini
├── test_setup.py           # Test script
├── setup.ps1               # Setup helper
├── run.ps1                 # Run helper
├── .env.example            # Contoh environment variables
├── .gitignore              # Git ignore rules
└── .streamlit/
    └── config.toml         # Streamlit config
```

## 🎨 Tips

### Upload Gambar Berkualitas
- Format: JPG, PNG
- Resolusi: Min 224x224px
- Ukuran: Max 200MB
- Pencahayaan: Baik, hindari silau

### Hasil Terbaik
- Gambar fokus pada area korosi
- Background jelas
- Tidak blur atau gelap
- Satu objek per gambar

## 🆘 Butuh Bantuan?

1. **Check README.md** untuk dokumentasi lengkap
2. **Check DEPLOYMENT.md** untuk deploy ke cloud
3. **Run test_setup.py** untuk diagnose masalah
4. **Check error message** di terminal

## 🎉 Selamat Mencoba!

Jika semua sudah setup, aplikasi akan terbuka di browser:
**http://localhost:8501**

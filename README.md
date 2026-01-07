# Sistem Deteksi dan Analisis Korosi

Aplikasi web berbasis Streamlit untuk mendeteksi korosi pada logam menggunakan Deep Learning dan analisis mendalam dengan AI.

## 🎯 Fitur Utama

- **Deteksi Korosi Otomatis**: Menggunakan model MobileNetV2 yang telah dilatih dengan akurasi ~87.77%
- **Analisis AI Mendalam**: Analisis visual komprehensif menggunakan Google Gemini AI
- **Laporan Terstruktur**: Mencakup 6 aspek analisis korosi
- **Interface User-Friendly**: Tampilan web yang intuitif dan mudah digunakan

## 📋 Aspek Analisis yang Dicakup

1. **Deteksi Perubahan Warna**: Mengidentifikasi area dengan perubahan warna abnormal
2. **Identifikasi Produk Korosi**: Mendeteksi karat, kerak, atau endapan
3. **Pitting (Korosi Sumuran)**: Mengidentifikasi lubang-lubang kecil pada permukaan
4. **Kerusakan Lapisan Pelindung**: Menilai kondisi coating/cat
5. **Deformasi Struktural**: Mengamati perubahan bentuk fisik
6. **Rekomendasi Tindakan**: Saran penanganan dan pencegahan

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone <repository-url>
cd corrosion
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Model

Letakkan file model `saved_model.keras` di direktori root project:

```
corrosion/
├── app.py
├── saved_model.keras  ← File model di sini
├── requirements.txt
└── README.md
```

### 4. Setup Gemini API Key

Dapatkan API key dari [Google AI Studio](https://makersuite.google.com/app/apikey), kemudian set sebagai environment variable:

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

Atau buat file `.env`:
```
GEMINI_API_KEY=your-api-key-here
```

## 🎮 Cara Menjalankan

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`

## 📖 Cara Menggunakan

1. **Upload Gambar**: Klik tombol upload dan pilih gambar objek logam (JPG/PNG)
2. **Tunggu Deteksi**: Model akan otomatis menganalisis gambar
3. **Lihat Hasil**: 
   - Status korosi (Ada/Tidak Ada)
   - Tingkat kepercayaan prediksi
4. **Analisis Mendalam**: Klik tombol "Lakukan Analisis Mendalam" untuk mendapatkan laporan AI
5. **Download Laporan**: Simpan hasil analisis dalam format teks

## 🏗️ Arsitektur Model

- **Base Model**: MobileNetV2 (pre-trained on ImageNet)
- **Transfer Learning**: Fine-tuned untuk deteksi korosi
- **Input Size**: 128x128 RGB
- **Output**: Binary classification (Korosi / Tidak Ada Korosi)
- **Akurasi**: 87.77%
- **Precision**: 92.55%
- **Recall**: 84.47%
- **F1 Score**: 88.32%

## 📁 Struktur Project

```
corrosion/
├── app.py                  # Aplikasi Streamlit utama
├── saved_model.keras       # Model terlatih (tidak termasuk di repo)
├── requirements.txt        # Dependencies Python
├── README.md              # Dokumentasi
└── .env                   # Environment variables (optional)
```

## 🔧 Konfigurasi

### Mengubah Model Path

Edit di `app.py`:
```python
model_path = "path/to/your/model.keras"
```

### Mengubah Input Size

Jika model Anda menggunakan ukuran input berbeda, ubah di fungsi `preprocess_image()`:
```python
img = image.resize((YOUR_SIZE, YOUR_SIZE))
```

### Menyesuaikan Class Labels

Sesuaikan mapping class di fungsi `predict_corrosion()`:
```python
# Class 0: CORROSION, Class 1: NOCORROSION
# Sesuaikan dengan training data Anda
```

## 🛠️ Troubleshooting

### Model tidak dapat dimuat
- Pastikan file `saved_model.keras` ada di direktori yang benar
- Cek kompatibilitas versi TensorFlow/Keras

### API Key Gemini tidak valid
- Verifikasi API key di [Google AI Studio](https://makersuite.google.com/app/apikey)
- Pastikan environment variable sudah di-set dengan benar

### Error saat upload gambar
- Pastikan format gambar adalah JPG/PNG
- Cek ukuran file tidak terlalu besar (max ~200MB)

## 📊 Contoh Output

### Deteksi Korosi
```
⚠️ KOROSI
Tingkat Kepercayaan: 94.25%

Analisis AI mencakup:
- Perubahan warna coklat kemerahan terdeteksi
- Produk korosi berupa karat pada permukaan
- Pitting diameter 2-3mm pada area tengah
- Coating mengalami pengelupasan 40%
- Rekomendasi: Tindakan segera diperlukan
```

### Tidak Ada Korosi
```
✅ TIDAK ADA KOROSI
Tingkat Kepercayaan: 91.80%

Analisis AI mencakup:
- Permukaan dalam kondisi baik
- Coating masih utuh dan protektif
- Tidak ada tanda-tanda degradasi
- Rekomendasi: Pemeliharaan rutin cukup
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan buat pull request atau laporkan issue.

## 📝 Lisensi

[MIT License](LICENSE)

## 👨‍💻 Author

**Robby Hardi Suryawiguna Mulyadi**
- NIM: 202022510033
- Project: AI untuk Deteksi Korosi

## 🙏 Acknowledgments

- Dataset: [Sample Rust Dataset](https://github.com/...)
- Model: MobileNetV2 (TensorFlow/Keras)
- AI Analysis: Google Gemini API
- Framework: Streamlit

## 📧 Kontak

Untuk pertanyaan atau saran, silakan hubungi melalui:
- Email: [your-email@example.com]
- GitHub: [@yourusername]

---

⭐ Jika project ini membantu, berikan star di GitHub!

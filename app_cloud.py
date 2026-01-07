"""
Versi Enhanced dengan Auto-Download Model dari Cloud
Untuk deployment ke Streamlit Cloud
"""
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import google.generativeai as genai
import os
import requests
from pathlib import Path

# Konfigurasi halaman
st.set_page_config(
    page_title="Sistem Deteksi Korosi",
    page_icon="🔍",
    layout="wide"
)

# Konfigurasi
MODEL_URL = os.getenv("MODEL_URL", "")  # URL untuk download model dari cloud
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
LOCAL_MODEL_PATH = "saved_model.keras"

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Download model dari cloud jika perlu
@st.cache_resource
def download_model_from_cloud():
    """Download model from cloud storage if not exists locally"""
    
    if os.path.exists(LOCAL_MODEL_PATH):
        return LOCAL_MODEL_PATH
    
    if not MODEL_URL:
        return None
    
    try:
        with st.spinner("📥 Downloading model from cloud... (first time only)"):
            response = requests.get(MODEL_URL, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            
            with open(LOCAL_MODEL_PATH, 'wb') as f:
                if total_size:
                    downloaded = 0
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        downloaded += len(chunk)
                        progress = downloaded / total_size
                        st.progress(progress)
                else:
                    f.write(response.content)
            
            st.success("✅ Model downloaded successfully!")
            return LOCAL_MODEL_PATH
            
    except Exception as e:
        st.error(f"❌ Error downloading model: {e}")
        return None

# Load model
@st.cache_resource
def load_model():
    """Load trained corrosion detection model"""
    try:
        # Try local first
        if os.path.exists(LOCAL_MODEL_PATH):
            model = tf.keras.models.load_model(LOCAL_MODEL_PATH)
            return model
        
        # Try download from cloud
        model_path = download_model_from_cloud()
        if model_path and os.path.exists(model_path):
            model = tf.keras.models.load_model(model_path)
            return model
        
        return None
        
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def preprocess_image(image):
    """Preprocess image for model prediction"""
    img = image.resize((128, 128))
    img_array = np.array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_corrosion(model, image):
    """Predict if image contains corrosion"""
    processed_img = preprocess_image(image)
    prediction = model.predict(processed_img, verbose=0)
    
    prob = prediction[0][0]
    predicted_class = 1 if prob > 0.5 else 0
    confidence = prob if prob > 0.5 else 1 - prob
    
    label = "KOROSI" if predicted_class == 0 else "TIDAK ADA KOROSI"
    
    return label, confidence * 100

def analyze_corrosion_with_ai(image, detection_result, confidence):
    """Analyze corrosion details using Gemini AI"""
    
    if not GEMINI_API_KEY:
        return "⚠️ API Key Gemini tidak ditemukan. Silakan set GEMINI_API_KEY di Secrets (untuk Streamlit Cloud) atau environment variables."
    
    try:
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        image_parts = [
            {
                "mime_type": "image/png",
                "data": img_byte_arr
            }
        ]
        
        if detection_result == "KOROSI":
            prompt = f"""Anda adalah ahli material dan korosi. Gambar ini telah dideteksi mengandung KOROSI dengan tingkat kepercayaan {confidence:.2f}%.

Lakukan analisis visual mendalam dan berikan laporan terstruktur yang mencakup:

1. **Deteksi Perubahan Warna**: 
   - Identifikasi area dengan perubahan warna yang tidak normal
   - Jelaskan jenis warna yang terlihat (merah/coklat/hijau/putih)
   - Interpretasi jenis korosi berdasarkan warna

2. **Identifikasi Produk Korosi**:
   - Jenis produk korosi yang terlihat (karat, kerak, endapan)
   - Lokasi dan distribusi produk korosi
   - Estimasi material yang terkorosi

3. **Pitting (Korosi Sumuran)**:
   - Ada/tidaknya lubang-lubang kecil pada permukaan
   - Tingkat keparahan pitting jika ada
   - Area yang paling terdampak

4. **Kerusakan Lapisan Pelindung**:
   - Kondisi coating/cat pada permukaan
   - Area yang mengalami pengelupasan atau retakan
   - Tingkat paparan logam dasar

5. **Deformasi dan Kerusakan Struktural**:
   - Perubahan bentuk fisik yang terlihat
   - Tonjolan, lekukan, atau deformasi lain
   - Potensi dampak pada integritas struktur

6. **Rekomendasi Tindakan**:
   - Tingkat urgensi penanganan (Rendah/Sedang/Tinggi/Kritis)
   - Langkah-langkah penanganan yang disarankan
   - Metode pencegahan untuk masa depan

Berikan analisis yang detail, profesional, dan mudah dipahami."""
        else:
            prompt = f"""Anda adalah ahli material dan korosi. Gambar ini telah dideteksi TIDAK mengandung korosi dengan tingkat kepercayaan {confidence:.2f}%.

Lakukan verifikasi visual dan berikan laporan yang mencakup:

1. **Kondisi Permukaan**:
   - Deskripsi kondisi permukaan secara umum
   - Warna dan tekstur yang terlihat
   - Ada/tidaknya tanda-tanda awal degradasi

2. **Penilaian Lapisan Pelindung**:
   - Kondisi coating/cat jika ada
   - Integritas lapisan pelindung
   - Area yang perlu perhatian khusus

3. **Faktor Risiko**:
   - Identifikasi area yang berpotensi rentan korosi
   - Faktor lingkungan yang perlu diperhatikan
   - Tanda-tanda peringatan dini jika ada

4. **Rekomendasi Pemeliharaan**:
   - Saran perawatan preventif
   - Frekuensi inspeksi yang disarankan
   - Langkah-langkah perlindungan tambahan

Berikan analisis yang objektif dan konstruktif."""
        
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([prompt, image_parts[0]])
        
        return response.text
        
    except Exception as e:
        return f"❌ Error dalam analisis AI: {str(e)}"

def main():
    st.title("🔍 Sistem Deteksi dan Analisis Korosi")
    st.markdown("""
    ### Aplikasi Deteksi Korosi Berbasis AI
    Upload gambar untuk mendeteksi keberadaan korosi dan mendapatkan analisis mendalam menggunakan AI.
    """)
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ Informasi")
        st.markdown("""
        **Cara Menggunakan:**
        1. Upload gambar objek logam
        2. Tunggu proses deteksi
        3. Lihat hasil dan analisis AI
        
        **Model:** MobileNetV2 Transfer Learning
        **Akurasi:** ~87.77%
        """)
        
        st.divider()
        
        st.markdown("""
        **Aspek Analisis:**
        - 🎨 Deteksi Perubahan Warna
        - 🔬 Identifikasi Produk Korosi
        - 🕳️ Pitting (Korosi Sumuran)
        - 🛡️ Kerusakan Lapisan Pelindung
        - ⚠️ Deformasi Struktural
        - 📋 Rekomendasi Tindakan
        """)
        
        st.divider()
        
        # System info
        with st.expander("🔧 System Status"):
            if os.path.exists(LOCAL_MODEL_PATH):
                st.success("✅ Model: Loaded")
            else:
                st.warning("⚠️ Model: Not found locally")
            
            if GEMINI_API_KEY:
                st.success("✅ API Key: Configured")
            else:
                st.error("❌ API Key: Not configured")
    
    # Load model
    model = load_model()
    
    if model is None:
        st.error("❌ Model tidak dapat dimuat.")
        st.info("""
        **Solusi:**
        - Pastikan file `saved_model.keras` ada di direktori yang sama
        - Atau set `MODEL_URL` di environment variables untuk auto-download
        """)
        return
    
    st.success("✅ Model berhasil dimuat!")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Upload gambar (JPG, JPEG, PNG)",
        type=["jpg", "jpeg", "png"],
        help="Upload gambar objek logam untuk dianalisis"
    )
    
    if uploaded_file is not None:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📷 Gambar yang Diupload")
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=True)
        
        with col2:
            st.subheader("🎯 Hasil Deteksi")
            
            with st.spinner("Menganalisis gambar..."):
                label, confidence = predict_corrosion(model, image)
            
            if label == "KOROSI":
                st.error(f"### ⚠️ {label}")
                st.metric("Tingkat Kepercayaan", f"{confidence:.2f}%")
                st.warning("Korosi terdeteksi pada gambar!")
            else:
                st.success(f"### ✅ {label}")
                st.metric("Tingkat Kepercayaan", f"{confidence:.2f}%")
                st.info("Tidak ada korosi yang terdeteksi pada gambar.")
        
        st.divider()
        
        # AI Analysis
        st.subheader("🤖 Analisis AI Mendalam")
        
        if st.button("🔍 Lakukan Analisis Mendalam", type="primary", use_container_width=True):
            with st.spinner("AI sedang menganalisis gambar secara detail..."):
                analysis = analyze_corrosion_with_ai(image, label, confidence)
            
            st.markdown(analysis)
            
            # Download analysis
            st.download_button(
                label="📥 Download Laporan Analisis",
                data=analysis,
                file_name=f"laporan_analisis_korosi_{uploaded_file.name}.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()

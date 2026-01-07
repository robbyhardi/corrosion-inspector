# Panduan Deploy ke Streamlit Cloud

## 📋 Persiapan

### 1. Siapkan Repository GitHub
- Push semua file ke GitHub repository
- Pastikan file `.gitignore` sudah benar
- **PENTING**: Jangan commit file model `.keras` (terlalu besar)

### 2. Upload Model ke Cloud Storage
Karena file model terlalu besar untuk GitHub, gunakan salah satu opsi:

#### Opsi A: Google Drive (Recommended)
1. Upload `saved_model.keras` ke Google Drive
2. Set sharing ke "Anyone with the link"
3. Dapatkan direct download link
4. Gunakan link tersebut di app

#### Opsi B: Hugging Face Hub
1. Buat akun di [Hugging Face](https://huggingface.co/)
2. Upload model ke Hugging Face Hub
3. Download dari app menggunakan `huggingface_hub`

#### Opsi C: GitHub Releases
1. Buat Release baru di GitHub
2. Attach file model ke release
3. Download dari URL release

## 🚀 Deploy ke Streamlit Cloud

### Step 1: Buat Akun Streamlit Cloud
1. Kunjungi [share.streamlit.io](https://share.streamlit.io/)
2. Sign in dengan GitHub account
3. Authorize Streamlit

### Step 2: Deploy App
1. Click "New app"
2. Pilih repository: `your-username/corrosion`
3. Branch: `main`
4. Main file path: `app.py`
5. Click "Deploy"

### Step 3: Set Secrets (API Key)
1. Di dashboard app, klik "Settings" → "Secrets"
2. Tambahkan:
```toml
GEMINI_API_KEY = "your-gemini-api-key-here"
```
3. Save

### Step 4: Update app.py untuk Load Model dari Cloud

Tambahkan function untuk download model:

```python
import requests
import os

@st.cache_resource
def download_model():
    """Download model from cloud if not exists"""
    model_path = "saved_model.keras"
    
    if not os.path.exists(model_path):
        st.info("Downloading model... (this may take a while)")
        
        # Option 1: From Google Drive
        gdrive_url = "YOUR_GDRIVE_DIRECT_LINK"
        
        # Download
        response = requests.get(gdrive_url)
        with open(model_path, 'wb') as f:
            f.write(response.content)
        
        st.success("Model downloaded!")
    
    return model_path
```

## 🔧 Troubleshooting

### Error: "Model file too large"
**Solusi**: Gunakan cloud storage dan download on-the-fly

### Error: "Out of memory"
**Solusi**: 
- Optimize model (model quantization)
- Gunakan model yang lebih kecil
- Upgrade ke Streamlit Cloud paid tier

### Error: "Secrets not found"
**Solusi**: 
- Check secrets di Settings → Secrets
- Pastikan format TOML correct
- Restart app

## 📊 Monitoring

### Check App Health
- Monitor di Streamlit Cloud dashboard
- Check logs untuk errors
- Monitor usage stats

### Update App
1. Push changes ke GitHub
2. Streamlit akan auto-redeploy
3. Check deployment status di dashboard

## 💰 Biaya

### Free Tier Limits:
- 1 GB RAM
- 1 CPU
- Public apps only
- Limited compute hours

### Paid Tier:
- More resources
- Private apps
- More compute hours
- Custom domains

## 🔒 Security Best Practices

1. **Never commit secrets** ke GitHub
2. **Use environment variables** untuk API keys
3. **Validate user inputs** di app
4. **Rate limiting** untuk API calls
5. **Monitor usage** untuk abuse

## 📝 Post-Deployment Checklist

- [ ] App berjalan tanpa error
- [ ] Model loading dengan benar
- [ ] API key working
- [ ] Upload gambar berfungsi
- [ ] Analisis AI berfungsi
- [ ] UI responsive
- [ ] Error handling proper
- [ ] Performance acceptable

## 🎯 Alternative Deployment Options

### 1. Heroku
- More control
- Support larger apps
- Paid service

### 2. AWS/GCP/Azure
- Full control
- Scalable
- More complex setup
- Higher cost

### 3. Railway.app
- Easy deployment
- Good free tier
- GitHub integration

### 4. Render
- Free tier available
- Easy deployment
- Good performance

## 📞 Support

Jika ada masalah:
1. Check Streamlit Community Forum
2. Check GitHub Issues
3. Contact Streamlit Support (paid users)

---

**Good luck with your deployment! 🚀**

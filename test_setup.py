"""
Script untuk testing komponen aplikasi
"""
import sys
import os

def test_imports():
    """Test semua import yang dibutuhkan"""
    print("🧪 Testing imports...")
    
    try:
        import streamlit
        print("✅ streamlit:", streamlit.__version__)
    except ImportError as e:
        print("❌ streamlit not found:", e)
        return False
    
    try:
        import tensorflow as tf
        print("✅ tensorflow:", tf.__version__)
    except ImportError as e:
        print("❌ tensorflow not found:", e)
        return False
    
    try:
        import numpy as np
        print("✅ numpy:", np.__version__)
    except ImportError as e:
        print("❌ numpy not found:", e)
        return False
    
    try:
        from PIL import Image
        print("✅ Pillow (PIL) imported successfully")
    except ImportError as e:
        print("❌ Pillow not found:", e)
        return False
    
    try:
        import google.generativeai as genai
        print("✅ google-generativeai imported successfully")
    except ImportError as e:
        print("❌ google-generativeai not found:", e)
        return False
    
    return True

def test_model_file():
    """Test keberadaan file model"""
    print("\n🧪 Testing model file...")
    
    model_paths = ["saved_model.keras", "saved_model.h5"]
    
    for path in model_paths:
        if os.path.exists(path):
            print(f"✅ Model found: {path}")
            size_mb = os.path.getsize(path) / (1024 * 1024)
            print(f"   Size: {size_mb:.2f} MB")
            return True
    
    print("❌ Model file not found")
    print("   Expected files: saved_model.keras or saved_model.h5")
    return False

def test_api_key():
    """Test keberadaan API key"""
    print("\n🧪 Testing Gemini API Key...")
    
    api_key = os.getenv("GEMINI_API_KEY")
    
    if api_key:
        print(f"✅ API Key found (length: {len(api_key)})")
        return True
    else:
        print("⚠️  API Key not set")
        print("   Set using: $env:GEMINI_API_KEY='your-api-key'")
        return False

def test_model_loading():
    """Test loading model"""
    print("\n🧪 Testing model loading...")
    
    try:
        import tensorflow as tf
        
        if os.path.exists("saved_model.keras"):
            model = tf.keras.models.load_model("saved_model.keras")
            print("✅ Model loaded successfully")
            print(f"   Input shape: {model.input_shape}")
            print(f"   Output shape: {model.output_shape}")
            return True
        elif os.path.exists("saved_model.h5"):
            model = tf.keras.models.load_model("saved_model.h5")
            print("✅ Model loaded successfully")
            print(f"   Input shape: {model.input_shape}")
            print(f"   Output shape: {model.output_shape}")
            return True
        else:
            print("⚠️  Model file not found, skipping load test")
            return False
            
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return False

def main():
    print("="*50)
    print("🔍 Corrosion Detection App - System Test")
    print("="*50)
    print()
    
    results = []
    
    # Test 1: Imports
    results.append(("Imports", test_imports()))
    
    # Test 2: Model File
    results.append(("Model File", test_model_file()))
    
    # Test 3: API Key
    results.append(("API Key", test_api_key()))
    
    # Test 4: Model Loading
    results.append(("Model Loading", test_model_loading()))
    
    # Summary
    print("\n" + "="*50)
    print("📊 Test Summary")
    print("="*50)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:.<30} {status}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print()
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! You're ready to run the app.")
        print("\nRun the app with: streamlit run app.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues before running the app.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

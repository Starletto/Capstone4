import streamlit as st
from PIL import Image

from src.model_loader import load_yolo_model
from src.detector import process_detection
from src.dashboard import render_vehicle_dashboard

st.set_page_config(
    page_title="Vehicle Detection Dashboard",
    page_icon="🚗",
    layout="wide",
)

#Model YOLO dimuat dari file best_model.pt
model = load_yolo_model("best_model.pt")

st.sidebar.title("🎛️ Panel Kontrol")
st.sidebar.markdown("---")


# Pengaturan confidence threshold untuk deteksi kendaraan
confidence_threshold = st.sidebar.slider(
    "Confidence Threshold", 
    min_value=0.0, 
    max_value=1.0, 
    value=0.25, 
    step=0.05,
    help="Atur ambang batas kepercayaan model untuk mendeteksi objek."
)

st.title("🚗 Vehicle Detection & Counting Dashboard")
st.write("Unggah gambar jalan raya untuk melihat hasil deteksi objek beserta statistik jumlah kendaraannya.")

#Membuat uploader untuk upload gambar kendaraan
uploaded_file = st.file_uploader(
    "Pilih gambar kendaraan...", 
    type=["jpg", "jpeg", "png"]
)

# Menampilkan hasil deteksi kendaraan jika file diupload dan model berhasil dimuat
if uploaded_file is not None and model is not None:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Gambar Asli yang Diupload")
        st.image(image)

    with col2:
        st.subheader("Hasil Deteksi Kendaraan")

        # Menjalankan deteksi kendaraan menggunakan model YOLO
        result, annotated_image = process_detection(model, image, confidence_threshold)
        st.image(annotated_image)

    #Menampilkan hasil deteksi
    render_vehicle_dashboard(result)

#Jika model gagal dimuat, tampilkan pesan error
else:
    if uploaded_file is None:
        st.info("Silakan unggah gambar untuk memulai deteksi kendaraan.")
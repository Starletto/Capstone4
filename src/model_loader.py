from ultralytics import YOLO
import streamlit as st
import os

#st cache resource untuk menyimpan model di cache
@st.cache_resource
def load_yolo_model(model_path: str = "best_model.pt"):
    ''' Membuat model YOLO '''
    # Mengecek apakah file model ada
    if not os.path.exists(model_path):
        st.error(f"file tidak ditemukan: {model_path}")
        return None

    #Memuat model YOLO
    try:
        model = YOLO(model_path)
        return model
    
    #Penanganan error
    except Exception as e:
        st.error(f"Gagal memuat model YOLO: {e}")

    return None
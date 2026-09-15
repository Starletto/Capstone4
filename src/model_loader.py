from ultralytics import YOLO
import streamlit as st
import os

@st.cache_resource
def load_yolo_model(model_path: str = "best_model.pt"):
    ''' Membuat model YOLO '''
    if not os.path.exists(model_path):
        st.error(f"file tidak ditemukan: {model_path}")
        return None

    try:
        model = YOLO(model_path)
        return model
    except Exception as e:
        st.error(f"Gagal memuat model YOLO: {e}")
    return None
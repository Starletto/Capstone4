# 🚗 Vehicle Detection & Counting App

Aplikasi berbasis web interaktif untuk mendeteksi kendaraan di jalan raya secara *real-time* menggunakan model Deep Learning (YOLO) serta dilengkapi dengan **Dashboard Statistik & Penghitungan Jumlah Kelas Kendaraan** secara otomatis. Proyek ini dikembangkan sebagai bagian dari **Capstone Project Module 4**.

---

## 📂 Struktur Direktori Project
Proyek ini dibangun menggunakan pendekatan **Modular Programming** agar kode lebih rapi, terstruktur, dan mudah dikembangkan (*maintainable*):

```text
my_vehicle_app/
│
├── app.py                 # File utama antarmuka (Frontend) Streamlit
├── best_model.pt          # Bobot model YOLO terbaik hasil fine-tuning
├── requirements.txt       # Daftar pustaka/library python yang dibutuhkan
│
└── utils/                 # Folder Modular Programming
    ├── __init__.py        # Penanda package python
    ├── model_loader.py    # Modul untuk memuat model YOLO (dengan Caching)
    ├── detector.py        # Modul untuk menangani inferensi & processing gambar
    └── dashboard.py       # Modul untuk merender dashboard statistik & hitung kendaraan

🛠️ Fitur Utama Aplikasi

    Interactive UI (Streamlit): Antarmuka web yang bersih, modern, dan mudah digunakan.

    Custom Object Detection: Mendeteksi 3 kategori kendaraan utama, yaitu:

        🚗 Car (Mobil)

        🚌 Bus (Bus)

        🚐 Van (Van)

    Confidence Threshold Slider: Pengguna dapat mengatur tingkat keyakinan (confidence) model secara dinamis langsung dari sidebar.

    Vehicle Counting Dashboard:

        Menghitung total keseluruhan kendaraan yang terdeteksi dalam satu gambar.

        Menampilkan rincian jumlah (count) untuk masing-masing kategori kendaraan secara terpisah menggunakan komponen metrik visual.

        Menyediakan tabel rincian data deteksi yang dapat diperluas (expandable table).

⚙️ Instalasi & Cara Menjalankan (Lokal)

Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi di komputer lokalmu:

    Clone Repository / Unduh Project
    Pastikan kamu sudah berada di dalam folder project.

    Buat & Aktifkan Virtual Environment (Opsional tapi Direkomendasikan)
    code Bash

    python -m venv .venv
    # Untuk Windows:
    .venv\Scripts\activate
    # Untuk Mac/Linux:
    source .venv/bin/activate

    Install Dependencies
    Instal semua library yang dibutuhkan menggunakan requirements.txt:
    code Bash

    pip install -r requirements.txt

    Pastikan File Model Tersedia
    Letakkan file bobot model hasil training kamu dengan nama best_model.pt di direktori utama project (sejajar dengan file app.py).

    Jalankan Aplikasi Streamlit
    code Bash

    streamlit run app.py

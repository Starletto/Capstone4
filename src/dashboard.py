import pandas as pd
import streamlit as st

def render_vehicle_dashboard(result):
    '''Function untuk menampilkan kendaraan yang terdeteksi'''

    st.markdown("---")
    st.markdown("### Hasil Deteksi Kendaraan")

    boxes = result.boxes

    # Jika box ada dan nilainya lebih dari 0
    if boxes is not None and len(boxes) > 0:

        # Mengambil ID kelas dan mengubahnya menjadi nama kelas
        box_classes = boxes.cls.cpu().numpy()
        class_names_dict = result.names
        detected_class_names = [class_names_dict[int(cls)] for cls in box_classes]

        # Menghitung jumlah kendaraan per kelas
        counts_df = pd.Series(detected_class_names).value_counts().reset_index()
        counts_df.columns = ['Kendaraan', 'Jumlah']

        # Menghitung total kendaraan 
        total_vehicles = len(box_classes)

        st.metric(
            label= "Total Kendaraan Terdeteksi",
            value= f"{total_vehicles} Unit"
        )

        #
        st.markdown("#### Jumlah Kendaraan per Kelas")

        cols = st.columns(len(counts_df))

        for idx, row in counts_df.iterrows():
            class_name = row['Kendaraan'].upper()
            total_count = row['Jumlah']

            with cols[idx]:
                st.metric(
                    label=f"Kategori: {class_name}",
                    value=f"{total_count} Unit"
                )

        with st.expander("Lihat Detail Deteksi"):
            st.dataframe(counts_df, use_container_width=True, hide_index=True)

    else:
        st.warning("Tidak ada kendaraan yang terdeteksi pada gambar ini.")
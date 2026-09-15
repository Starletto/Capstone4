import numpy as np

def process_detection(model, image, confidence_threshold: float):
    ''' Function untuk menjalankan prediksi model, 
        dan mengembalikan hasil deteksi yang 
        telah ditambahkan bounding box             '''

    # Menjalankan prediksi model YOLO
    results = model(image, conf=confidence_threshold)
    result = results[0]

    #Membuat bounding box pada gambar
    annotated_image = result.plot()

    return result, annotated_image
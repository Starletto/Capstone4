import numpy as np

def process_detection(model, image, confidence_threshold: float):
    ''' Function untuk menjalankan prediksi model, 
        dan mengembalikan hasil deteksi yang 
        telah ditambahkan bounding box             '''

    results = model(image, conf=confidence_threshold)
    result = results[0]

    annotated_image = result.plot()

    return result, annotated_image
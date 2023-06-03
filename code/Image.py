import cv2

def guardar_primer_fotograma(video_path, output_path):
    # Cargar el video
    video = cv2.VideoCapture(video_path)

    # Leer el primer fotograma
    ret, frame = video.read()

    # Verificar si se pudo leer el fotograma correctamente
    if ret:
        # Guardar el primer fotograma en el archivo de salida
        cv2.imwrite(output_path, frame)
        print("Primer fotograma guardado correctamente.")
    else:
        print("No se pudo leer el primer fotograma.")

    # Liberar el objeto de video
    video.release()

# Ruta del video de entrada
video_path = "resource/video.mp4"

# Ruta de salida para guardar el primer fotograma
output_path = "resource/primer_fotograma.jpg"

# Llamar a la función para guardar el primer fotograma
guardar_primer_fotograma(video_path, output_path)

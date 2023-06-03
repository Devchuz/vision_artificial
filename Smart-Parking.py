import cv2
import pickle
import numpy as np

vagas = []
with open('estacionamento.pkl', 'rb') as arquivo:
    vagas = pickle.load(arquivo)

video = cv2.VideoCapture('resource/video.mp4')

fps = video.get(cv2.CAP_PROP_FPS)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_path = 'resultado.mp4'

# Crear el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec de video para el formato MP4
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

while True:
    check, img = video.read()
    if not check:
        break

    ImgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(ImgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedia = cv2.medianBlur(imgTh, 5)
    kernel = np.ones((3, 3), np.int8)
    ImgDil = cv2.dilate(imgMedia, kernel)

    Es_Disponibles = 0
    for x, y, w, h in vagas:
        vaga = ImgDil[y:y + h, x:x + w]
        count = cv2.countNonZero(vaga)
        cv2.putText(img, str(count), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        if count < 900:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            Es_Disponibles += 1
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(img, (90, 0), (415, 60), (0, 255, 0), -1)
        cv2.putText(img, f'Libre: {Es_Disponibles}/69', (95, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

    out.write(img)  # Escribir el cuadro procesado en el video de salida

    cv2.imshow('video', img)
    cv2.imshow('videoTh', ImgDil)

    if cv2.waitKey(10) == ord('q'):
        break

# Liberar los recursos y cerrar el video de salida
out.release()
cv2.destroyAllWindows()
video.release()

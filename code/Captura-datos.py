import pickle

import cv2
img = cv2.imread("primer_fotograma.jpg")

vagas = []

for x in range(69):

    vaga = cv2.selectROI('Estacionamiento',img,False)
    cv2.destroyWindow('Estacionamoemto')
    vagas.append(vaga)

    for x,y,w,h in vagas:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

with open('Estacionamiento.pkl','wb') as arquivos:
    pickle.dump(vagas,arquivos)
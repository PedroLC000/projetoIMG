import numpy as np
import cv2 as cv
import os

# caso necessário que seja removido todos os outros vídeos do diretório
# for f in os.scandir('videos'):
#     os.remove(f)

cap = cv.VideoCapture(0)

# Define o codec e crie o objeto VideoWriter
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('videos/gravacao.avi', fourcc, 20.0, (640,  480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Erro!")
        break

    # Salva o frame para formar o vídeo
    out.write(frame)

    # Vizualização da imagem na câmera
    cv.imshow('frame', frame)

    # Finaliza a vizualização na câmera
    if cv.waitKey(1) == ord('q'):
        break

# Libera e finaliza tudo
cap.release()
out.release()
cv.destroyAllWindows()
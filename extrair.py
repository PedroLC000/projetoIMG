import cv2
import math
import os

i = 0

# Remove todos os frames anteriores do diretório
for f in os.scandir('frames'):
    os.remove(f)

for filename in os.scandir('videos'):

    # Conecta a câmera ou o caminho de um vídeo.
    cap = cv2.VideoCapture(filename.path)
    frameRate = cap.get(5)
    
    while(cap.isOpened()):

        frameId = cap.get(1)

        # Verifica quadro a quadro.
        ret, frame = cap.read()

        # Essa condição previne que o loop termine caso o video acabe. 
        if ret == False:
            break
        
        #Salva um frame por segundo na pasta frames.
        if (frameId % math.ceil(frameRate) == 0):
            cv2.imwrite('frames\Frame'+str(i)+'.jpg', frame)
            i += 1

    # Libera o dispositivo que está sendo usado e destroi as janelas criadas.
    cap.release()

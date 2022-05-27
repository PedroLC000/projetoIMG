#Blibiotecas
import cv2

# Conecta a câmera ou o caminho de um vídeo.
cap = cv2.VideoCapture('videos/gravacao.avi')
i = 0
 
while(cap.isOpened()):
    # Verifica quadro a quadro.
    ret, frame = cap.read()

    # Essa condição previne que o loop termine caso o video acabe. 
    if ret == False:
        break
    
    #Salva frame por frame na pasta frames.
    cv2.imwrite('frames\Frame'+str(i)+'.jpg', frame)
    i += 1

# Libera o dispositivo que está sendo usado e destroi as janelas criadas.
cap.release()

#blibiotecas
import cv2
import numpy as np

image = cv2.imread('frames/Frame20.jpg')
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply binary thresholding c/ método simples
# ret, thresh = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)

# binary thresholding c/ método otsu
ret, thresh = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
 
# salva a imagem binarizada
cv2.imwrite('saves/image_thres1.jpg', thresh)

# Aplica a morfologia matemática (operação de abertura)
kernel = np.ones((5,5),np.uint8)
abertura = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cv2.imwrite('saves/image_opening.jpg', abertura)

# detecta contornos na imagem binarizada usando cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=abertura, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# lista todos os vetores de contornos
# for cont, i in enumerate(contours):
#   print(len(i), cont)

# desenha o contorno na imagem original 
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
                
# save the results
cv2.imwrite('saves/contours_none_image3.jpg', image_copy)


import cv2
import numpy as np
import mahotas as mt
import os
import pandas as pd

image = cv2.imread('frames/Frame20.jpg')
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# binary thresholding c/ método otsu
# ret, thresh = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# cv2.imwrite('saves/image_thres1.jpg', thresh)

# aplica a morfologia matemática (operação de abertura)
# kernel = np.ones((3,3),np.uint8)
# abertura = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
# cv2.imwrite('saves/image_opening.jpg', abertura)

blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
wide = cv2.Canny(blurred, 10, 200)
cv2.imwrite('saves/image_wide.jpg', wide)

# detecta contornos na imagem binarizada usando cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=wide, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# desenha o contorno na imagem original 
image_copy = image.copy()
# cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
# cv2.imwrite('saves/contours_none_image.jpg', image_copy)

x, y = [], []

# utilizado para extrair cada imagem encontrada com o algoritmo de fremman
for count, contour_line in enumerate(contours):
    x, y = [], []
    if len(contour_line) > 80:
        for contour in contour_line:
            x.append(contour[0][0])
            y.append(contour[0][1])

        x1, x2, y1, y2 = min(x), max(x), min(y), max(y)
        cropped = image[y1:y2, x1:x2]
        cv2.imwrite(f'saves/crop/crop{count}.png',cropped)
        x.clear()
        y.clear()


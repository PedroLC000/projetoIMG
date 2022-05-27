#blibiotecas
import cv2

image = cv2.imread('/content/Frame20.jpg')
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# binary thresholding simples
ret, thresh = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY) 

# salva a imagem binarizada
cv2.imwrite('image_thres1.jpg', thresh)

# detecta contornos na imagem binarizada usando cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# lista todos os vetores de contornos
# for cont, i in enumerate(contours):
#   print(len(i), cont)

# desenha o contorno na imagem original 
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
                
# save the results
cv2.imwrite('contours_none_image1.jpg', image_copy)

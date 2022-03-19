import cv2
import os

img_name = os.listdir('data/masks/')
for img in img_name:
    if img=='.keep':
        continue
    imgB = cv2.imread('data/masks/'+img)
    print(img)
    imgB = imgB/255
    imgB = imgB.astype('uint8')
    cv2.imwrite(os.path.join('data/mask01/'+img),imgB)


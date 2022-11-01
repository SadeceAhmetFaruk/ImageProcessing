import cv2
import numpy as np
from numpy import shape, zeros

h = 500
w = 400

original = cv2.imread('12.jpg')
original = cv2.resize(original,(w,h))

image = cv2.imread('12.jpg',0)
image = cv2.resize(image,(w,h))

[h,w] = shape(image)
image2 = zeros([h,w], dtype=np.uint8)

max = 0

#maximumu bulma
for i in range (h):
    for j in range (w):
        if max < image [i,j]:
            max = image [i,j]


#maximumdan görüntü matrisinin her değerini çıkarma
for i in range (h):
    for j in range (w):
        image2[i,j] = max - image[i,j]


cv2.imshow("original", original)
cv2.imshow("gri",image)
cv2.imshow("ters cevrilmis",image2)
cv2.waitKey()


#hazır kütüphane kullanarak oluşturlması
'''inverted = np.invert(image)
cv2.imshow("inverted",inverted)
cv2.waitKey()'''
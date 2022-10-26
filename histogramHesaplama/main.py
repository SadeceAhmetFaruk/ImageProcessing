
import cv2
from matplotlib import pyplot as plt
from numpy import zeros, shape


foto = cv2.imread("12.jpg",0)

Hist = zeros(256)
[w,h] = shape(foto)

for i in range (0,w):
    for j in range (0,h):
        a = foto[i,j]
        Hist[a] = Hist[a] + 1

plt.plot(Hist)
#plt.stem(Hist)
plt.show()

cv2.imshow("fotograf", foto)
cv2.waitKey()


#Hazır Fonksiyon
'''foto = cv2.imread("ev.jpg",0)
hist = cv2.calcHist([foto], [0],None,[256], [0,256])
#plt.figure(1)
plt.plot(hist)
plt.show()

cv2.imshow("ev",foto)
cv2.waitKey()'''


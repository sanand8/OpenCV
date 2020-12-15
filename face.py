import cv2
import numpy as np


faceCase= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
path = 'resource/fav.jpg'
img1 = cv2.imread(path)
w,h = 480,480
img = cv2.resize(img1,(w,h))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCase.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow("original image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
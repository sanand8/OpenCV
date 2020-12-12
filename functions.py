import cv2
import numpy as np

img = cv2.imread("resource/gate_image.jpg")

#to change the color of the pic
Gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#to convert into blurred image
Blur_img = cv2.GaussianBlur(img,(7,7),0)

#to detect the edges in pic
Canny_img = cv2.Canny(img,100,100)

kernel = np.ones((5,5),np.uint8)
#to add thickness
Dilation = cv2.dilate(Canny_img,kernel,iterations=4)

#to decrease the thickness
Erode = cv2.erode(Dilation,kernel,iterations=10)
width = 300
height = 300 
dsize = (width,height)
new_img = cv2.resize(Erode, dsize, interpolation=cv2.INTER_AREA)
cv2.imshow("my wind", new_img)
cv2.waitKey(0)
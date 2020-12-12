import cv2
import numpy as np

img1 = np.zeros((512,512,3),np.uint8)

#the colon inside [] this is to color the whole screen
#img1[:] = 255,0,0

#it used to draw line the first is for image 
#second is starting and third is for ending 
#fourth is for color and last for thickness
cv2.line(img1,(0,0),(img1.shape[1],img1.shape[0]),(0,255,0),3)

#draw rectangle
cv2.rectangle(img1,(0,0),(300,300),(0,0,255),cv2.FILLED)

#draw circle
cv2.circle(img1,(400,300),35,(255,255,0),3)

#put text 330,330 is the starting point
# nxt one is font type and then scale thn color and last thickness 
cv2.putText(img1,"OpenCV ",(330,330),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.imshow("image",img1)
cv2.waitKey(0)
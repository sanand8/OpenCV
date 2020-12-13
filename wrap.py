import cv2
import numpy as np

img1 = cv2.imread("resource/kings.jpg")
#img = cv2.resize(img1,(480,300))

width,height = 250,350
#coordinates of the card
pts1 = np.float32([[2152,2194],[2788,1224],[1133,547],[460,1393]])

#fixing the matrix for the card
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#for required transformation
matrix = cv2.getPerspectiveTransform(pts1,pts2)

#fixing the height and width 
imgout = cv2.warpPerspective(img1,matrix,(width,height))

cv2.imshow("image",imgout)
cv2.waitKey(0)
cv2.imshow("image",img1)
cv2.waitKey(0)
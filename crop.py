import cv2
print("package imported")

#reading image
img = cv2.imread("resource/gate_image.jpg")
print(img.shape)

imgResize = cv2.resize(img,(480,300))
print(imgResize.shape)

cropped = imgResize[0:200,200:300]

cv2.imshow("my wind",cropped)
cv2.waitKey(0)
cv2.imshow("my wind",imgResize)
cv2.waitKey(0)

#cv2.waitKey(0)
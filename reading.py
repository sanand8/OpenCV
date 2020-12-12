import cv2
print("package imported")

#reading image
img = cv2.imread("resource/gate_image.jpg")

#resizing the image 
width = 300
height = 300 
dsize = (width,height)
new_img = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)
#display the image
#first argument is for the window and secnd the image name
cv2.imshow("Output",new_img)

#it will confirm how much time you want to show the image
cv2.waitKey(0)

#import the video
cap = cv2.VideoCapture("resource/tom.mp4")

#now display since it is a sequence of images so

while True:
    success, img1 = cap.read()
    cv2.imshow("video", img1)
    #0xFF is a bit mask represents 8 bit binary
    # and we nee only integer below 255 to represent a character 
    if cv2.waitKey(50) & 0xFF == ord('s'):
        break

#here the 0 is for the camera 
cam = cv2.VideoCapture(0)
#now setting the height and width
#first one is the id e.g 3 for width and 4 for height
cam.set(3,640)
cam.set(4,480)
cam.set(10,1000)
while True:
    success, img2 = cam.read()
    #print(success)
    cv2.imshow("video", img2)
    #0xFF is a bit mask represents 8 bit binary
    # and we nee only integer below 255 to represent a character 
    if cv2.waitKey(50) & 0xFF == ord('s'):
        break
import cv2
import numpy as np

#stacking images
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#for getting the shape
def getContor(img):
    #findContor will find the shape and retr external will find the outtermost boundary
    #cv2.chain will gives all the boundary points of the shape 
    #countours is the list of countours and hierarchy show the relationship of the nested figures
    contours,Hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        #it will find the area
        area = cv2.contourArea(cnt)
        print(area)
        if area>19:
            #it will draw the countour shape
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)

            #it will give the arc length and second argument shows that it is closed
            per2 = cv2.arcLength(cnt,True)
            #print(per2)

            #this function will approximate the shape if it is detected bad figure
            #it returns the coordinates
            approx = cv2.approxPolyDP(cnt,0.02*per2,True)

            #corner of the objects detected
            objCorner = len(approx)

            #it will bound the the figure into a rectangle and x,y are top left coordinates
            x, y, w, h = cv2.boundingRect(approx)

            if objCorner == 4:
                aspRatio = w/float(h)
                if aspRatio>0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"

            elif objCorner == 5:
                objectType = "Pentagon"  
            else:
                objectType = "None"

            #used to draw rectangle over the image
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)




path = 'resource/shapes.png'
img = cv2.imread(path)
imgBlank = np.zeros_like(img)
imgContour = imgBlank.copy()
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(gray_img,(7,7),1)

imgCanny = cv2.Canny(img_blur,50,50)

#now it will get the shape of the objects
getContor(imgCanny)
imgStack = stackImages(0.6,([img,gray_img,img_blur],[imgCanny,imgContour,imgBlank]))

# cv2.imshow("my image",img)
# cv2.imshow("gray",gray_img)
# cv2.imshow("blur",img_blur)
cv2.imshow("stacked images",imgStack)
cv2.waitKey(0)
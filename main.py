import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap=cv2.VideoCapture(0)
cap.set(3,640) #width
cap.set(4,480) #height
segmentor = SelfiSegmentation()
fpsreader = cvzone.FPS()
cap.set(cv2.CAP_PROP_FPS,60)
imbg = cv2.imread("images/1.jpg")
listimg =os.listdir("images")
print(listimg)

imglist=[]
for imgpath in listimg:
    img=cv2.imread(f'images/{imgpath}')
    imglist.append(img)
print(len(imglist))

indexImg=0

while True:
    success, img = cap.read()
    imgout = segmentor.removeBG(img,imglist[indexImg],threshold=0.7)
    imgstacked=cvzone.stackImages([img,imgout],2,1)
    _,imgstacked = fpsreader.update(imgstacked,color=(0,0,255))


    cv2.imshow("image",imgstacked)
    #cv2.imshow("img out", imgout)
    print(indexImg)
    key=cv2.waitKey(1)
    if key== ord('a'):
        if indexImg >0:
            indexImg -=1
    elif key== ord('d'):
        if indexImg < len(imglist)-1:
            indexImg +=1
    elif key== ord('q'):
        break




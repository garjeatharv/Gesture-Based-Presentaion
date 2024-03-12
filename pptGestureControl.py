import os
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

#Parameters
width, height = int(1280),int(720)
folderPath = "D:\VS CODE\Python\Gesture PPT\Presentation"

#camera setup
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

#variables
imgNumber = 3
hs,ws = int(120*1),int(213*1)
gestureThreshold = 300 
buttonPressed = False
buttonCounter = 0
buttonDelay = 30
annotations = [[]]
annotationNumber = 0
annotationStart = False

#Hand Decator
detector = HandDetector(detectionCon=0.8,maxHands=1)

#get list of presntaion images
pathImage = sorted(os.listdir(folderPath), key=len)
# print(pathImage)

while True:

    #import Images
    success, img = cap.read()
    img = cv2.flip(img,1)
    pathFullImage = os.path.join(folderPath,pathImage[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    # Hand
    hands, img = detector.findHands(img)
    cv2.line(img,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),10)
    if hands and buttonPressed is False:
        hand = hands[0]
        fingures = detector.fingersUp(hand)
        cx,cy = hand['center']
        # print(fingures)

        lmList = hand['lmList']

        #constrain for easier draw
        xVal = int(np.interp(lmList[8][0],[width//2,w],[0,width]))
        yVal = int(np.interp(lmList[8][1],[150,height-150],[0,height]))
        indexFingure = xVal,yVal
        

        if cy<= gestureThreshold: #if hand is above face
            annotationStart = False
            #gesture 1- Previous Slide (Thumb emoji)
            if fingures == [1,0,0,0,0]:
                print("Left")
                annotationStart = False
                if imgNumber>0:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber-=1
            
            #gesture 2- Right Slide (Pinky fingure out)
            if fingures == [0,0,0,0,1]:
                print("Right")
                annotationStart = False
                if imgNumber< len(pathImage)-1:
                    buttonPressed = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber+=1
       
        #Gesture 3 - Show Pointer (Index fingure and Middle fingure up)
        if fingures == [0,1,1,0,0]:
            cv2.circle(imgCurrent, indexFingure,12,(0,0,255),cv2.FILLED)
            annotationStart = False

        #Gesture 4 - Draw Pointer (Index Fingure up)
        if fingures == [0,1,0,0,0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber +=1
                annotations.append([])
            cv2.circle(imgCurrent, indexFingure,12,(0,0,255),cv2.FILLED)
            annotations[annotationNumber].append(indexFingure)
        else:
            annotationStart = False

        #Gesture 5 - Erase (Index fingure, Middle Fingure and Ring fingure up)
        if fingures == [0,1,1,1,0]:
            if annotations:
                if annotationNumber>=0:
                    annotations.pop(-1)
                    annotationNumber-=1
                    buttonPressed=True
    else:
        annotationStart =False
    #Button Pressed itterations
    if buttonPressed:
        buttonCounter +=1
        if buttonCounter> buttonDelay:
            buttonCounter = 0
            buttonPressed = False


    for i in range (len(annotations)):
        for j in range (len(annotations[i])):
            if j!=0:
                cv2.line(imgCurrent,annotations[i][j-1],annotations[i][j],(0,0,200),12)


    #Adding webcam img on the slide
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws: w] = imgSmall

    cv2.imshow("Slides",imgCurrent)
    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

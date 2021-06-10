import cv2
import webbrowser
import math
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,500)

detector = htm.HandDetector()
face_book = False
you_tube = False
while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPostion(img,draw=False)
    if len(lmList) != 0:
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        x3,y3 = lmList[12][1],lmList[12][2]
        length1 = math.hypot(x2-x1,y2-y1)
        lenght2 = math.hypot(x3-x2,y3,y2)
        if length1>120 and length1<170:
            cv2.putText(img,"OK",(10,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
            if not face_book:
                webbrowser.open("https://facebook.com")
                face_book = True
        elif lenght2>280 and lenght2<320:
            cv2.putText(img,"OK",(10,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
            if not you_tube:
                webbrowser.open("https://youtube.com")
                you_tube = True
    cv2.imshow("output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
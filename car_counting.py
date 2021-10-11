import cv2
import numpy as np

vid = cv2.VideoCapture("yourFilePath")
backsub = cv2.createBackgroundSubtractorMOG2()
counter = 0

while True:
    ret,frame = vid.read()

    if ret:

        fgmask = backsub.apply(frame)
        cv2.line(frame,(50,0),(50,300),(0,255,0),2)
        cv2.line(frame, (70, 0), (70, 300), (0, 255, 0),2)

        counturs,hierarchy  = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try :hierarchy = hierarchy[0]
        except: hierarchy = []


        for contour,hier in zip(counturs,hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w > 40 and h > 40:
                cv2.rectangle(frame,(x,y),(x+w,y +h),(255,0,0),3) #lefttop ve right bottom coordinates
                if x >50 and x<70:
                    counter+=1

        cv2.putText(frame, "car:" +str(counter),(90,100),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2,cv2.LINE_AA)



        cv2.imshow("car counter",frame)
        cv2.imshow("fgmask",fgmask)


        if cv2.waitKey(20) & 0xFF == ord("q"):
            break


vid.release()
cv2.destroyAllWindows()
import cv2

video= cv2.VideoCapture("bb3.mp4")

tracker=cv2.TrackerCSRT_create()
print("what is tracker", tracker)

#capturing indivisual frame in video
returned,img=video.read()


# creating bounding box to object we have to track
b_box=cv2.selectROI("tracking",img,False)
# intilizing the tracker on the image and the b_box
tracker.init(img,b_box)

print("what is b_box value" ,b_box)

def drawBoxPosition(img,b_box):
    x,y,w,h=int(b_box[0]), int(b_box[1]), int(b_box[2]), int(b_box[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)), (255,0,255),3,1)
    cv2.putText(img, "Tracking", (100,100), cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),2)

while True:
    dummy,img= video.read()

    #updating tracker
    success,b_box=tracker.update(img)
    #true
    if success:
        drawBoxPosition(img,b_box)


    else:
        cv2.putText(img,"tracking is lost", (100,100), cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0),2)


    cv2.imshow("output", img)

    if cv2.waitKey(25) == 32:
        print("stopped")
        break

video.release()
cv2.destroyAllWindows()
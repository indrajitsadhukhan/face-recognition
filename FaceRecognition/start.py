import cv2 
#Load some pre-trained data on face frontals from opencv (haarcascade algorithm)
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
p=k=0
webcam=cv2.VideoCapture('Videos/meeting.mp4')
while True:
    successful_frame_read,frame=webcam.read()
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    p=k
    #DETECT FACES
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    k=len(face_coordinates)
    if(p!=k):
        print(len(face_coordinates))
    cv2.imshow('First',cv2.resize(frame,(1300,700)))
    cv2.waitKey(1)
    if(cv2.getWindowProperty('First',cv2.WND_PROP_VISIBLE)==0):
        break
webcam.release()
print("Code completed") 









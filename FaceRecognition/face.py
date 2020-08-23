import cv2
import face_recognition 
import numpy as np
import os
file=[]
i=0
faceEncoding=[]


source = '/home/indrajit/PROJECTS/FaceDetection/images/mark'
for filename in os.scandir(source):
    if(filename.path.endswith(".jpg") or filename.path.endswith(".png") or filename.path.endswith(".jpeg")):
        img1=face_recognition.load_image_file(os.path.join(source,filename))
        img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        faceEncoding.append((face_recognition.face_encodings(img1)[0],img1))
        i=i+1



print(len(faceEncoding))

flag=False
img2=face_recognition.load_image_file('images/tim2.jpg')
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
for faceLoc2 in face_recognition.face_locations(img2):
    cv2.rectangle(img2,(faceLoc2[3],faceLoc2[0]),(faceLoc2[1],faceLoc2[2]),(0,255,0),2)
faceEncod2=face_recognition.face_encodings(img2)

results=[]
print(len(faceEncod2))
faceLoc=face_recognition.face_locations(img2)
for i in range(0,len(faceEncod2)):
    for j in range(0,len(faceEncoding)):
        if(face_recognition.compare_faces([faceEncoding[j][0]],faceEncod2[i])[0]==True and flag==False ):
         
            cv2.putText(img2,'MARK JUCKERBERG',(faceLoc[i][3]-50,faceLoc[i][0]-35),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
            flag=True
cv2.imshow('Image2',cv2.resize(img2,(1000,800)))
cv2.waitKey(0)
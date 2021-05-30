# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:57:09 2021

@author: akira
"""

import cv2 as cv


cap = cv.VideoCapture(0) #laptop内蔵カメラ起動

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')

while True:
    ret, frame = cap.read() #内蔵カメラで取得したキャプチャーをフレーム化
    
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY) #写真をグレー化
    faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(100, 100)) #顔認識人数分

 #   print(len(faces))
    
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) #顔認識部分を青色で囲う
        eye_gray = gray[y:y+h, x:x+w] #顔部分をグレー化
        eye_color = frame[y:y+h, x:x+w] #顔部分を取り出し
        eyes = eye_cascade.detectMultiScale(eye_gray,minSize=(50, 50))

        smiles= smile_cascade.detectMultiScale(eye_gray,scaleFactor= 1.2, minNeighbors=10, minSize=(20, 20))#笑顔識別
        if len(smiles) >0 :
            for(sx,sy,sw,sh) in smiles:
                cv.circle(frame,(int(x+sx+sw/2),int(y+sy+sh/2)),int(sw/2),(0, 0, 255),2)#red


        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2) #目認識部分を緑色で囲う
    
    
    cv.putText(frame, f'persons={len(faces)}', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), thickness=2)
#    cv.putText(frame, f'eyes={len(eyes)}', (50, 100), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), thickness=2)

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()    
cv.destroyAllWindows()



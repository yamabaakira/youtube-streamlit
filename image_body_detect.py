import cv2 as cv
import streamlit as st
from PIL import Image
import numpy as np

def detect_image(detections):
    for (x, y, w, h) in detections:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #顔認識部分を青色で囲う

    st.write('検出後画像')
    st.write(f"""{option}検出人数：{len(detections)}人検出""")
    st.image(img)


st.title('人検出アプリ　opencv/streamlit')
body_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


uploaded_file = st.file_uploader('Choose an image...',type = ['jpg'])
option = st.selectbox(
    'detction box:',
    ('face', 'body')
)

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    img = np.array(image)

    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY) #写真をグレー化

    if option == 'face':
        detections = face_cascade.detectMultiScale(gray, 1.3, 5) #人数分
    elif option == 'body':
        detections = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(200, 200)) #人数分

    detect_image(detections)




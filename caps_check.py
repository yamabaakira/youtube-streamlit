import cv2 as cv
import streamlit as st
from PIL import Image
import numpy as np

st.title('image比較アプリ　opencv by ymb')

# col1, col2 = st.beta_columns(2)
# with col1:
#     st.header("EA9")
#     st.image("image/SC_120607165103.jpg")

# with col2:
#     st.header("CM5")
#     st.image("image/SC_120607165128.jpg")


uploaded_file_EA9 = st.file_uploader('Choose an EA9 image...',type = ['jpg']) #jpgファイル読込み
if uploaded_file_EA9 is not None:
    image_EA9=Image.open(uploaded_file_EA9)
    img_EA9 = np.array(image_EA9)
    st.image(img_EA9)
    img_EA9_reshape = img_EA9[70 : 480,]

uploaded_file_CM5 = st.file_uploader('Choose an CM5 image...',type = ['jpg']) #jpgファイル読込み
if uploaded_file_CM5 is not None:
    image_CM5=Image.open(uploaded_file_CM5)
    img_CM5 = np.array(image_CM5)
    st.image(img_CM5)
    st.write(img_CM5.shape)
    img_CM5_reshape = img_CM5[70 : 480,]

if uploaded_file_EA9 and uploaded_file_CM5 is not None:
    if st.button('画像比較'):
        compare_caps = np.array_equal(img_EA9_reshape,img_CM5_reshape)
        if compare_caps == True:
            st.write('照合OK')
        else:
            st.write('照合NG')


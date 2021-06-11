import cv2 as cv
import streamlit as st
from PIL import Image
import numpy as np

st.title('EA9 CM5 キャプチャ比較　by YMB')

col1, col2 = st.beta_columns(2)#EA9とCM5の画像を2カラムで表示
with col1:
   uploaded_file_EA9 = st.file_uploader('Choose an EA9 image...',type = ['jpg','bmp']) #jpg,bmpファイル読込み
   if uploaded_file_EA9 is not None:
        image_EA9 = Image.open(uploaded_file_EA9)
            
        img_EA9_resize = image_EA9.resize((320, 240))
        st.image(img_EA9_resize) #選択したファイルを半分にリサイズして表示

        img_EA9 = np.array(image_EA9)#読取ったbmpをnumpy配列に入れる
        img_EA9_reshape = img_EA9[70 : 480,] #画面ヘッダー部分を切取り 

with col2:
    uploaded_file_CM5 = st.file_uploader('Choose an CM5 image...',type = ['jpg','bmp']) #jpg,bmpファイル読込み
    if uploaded_file_CM5 is not None:
        image_CM5 = Image.open(uploaded_file_CM5)

        img_CM5_resize = image_CM5.resize((320, 240))
        st.image(img_CM5_resize) #選択したファイルを半分にリサイズして表示

        img_CM5 = np.array(image_CM5)#読取ったbmpをnumpy配列に入れる
        img_CM5_reshape = img_CM5[70 : 480,] #画面ヘッダー部分を切取り     


if uploaded_file_EA9 and uploaded_file_CM5 is not None:
    if st.button('画像比較'):#EA9とCM5の画像比較開始PB押下
        compare_caps = np.array_equal(img_EA9_reshape,img_CM5_reshape)#EA9とCM5の画像比較
        if compare_caps == True:
            st.write('照合OK')#EA9とCM5同じ配列
        else:
            st.write('照合NG')  
            img_diff = img_EA9_reshape.astype(int) - img_CM5_reshape.astype(int) 
            img_diff_abs = np.abs(img_diff)
            st.image(img_diff_abs)

                 


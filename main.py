import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')

st.write('DataFrame1')

video_file = open('CLICK Ethernet PLC  Quick Start.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

mp3_file = open('YOASOBI夜に駆ける.mp3', 'rb')
mp3_bytes = mp3_file.read()
st.audio(mp3_bytes,format="audio/wav")

#img = Image.open('DSC_1153.jpg')
#st.image(img, caption='yamaba', use_column_width=True)

#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat','lon']
#)
#st.map(df)
#st.dataframe(df.style.highlight_max(axis=0))

#st.table(df.style.highlight_max(axis=0))
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)




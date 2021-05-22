import pandas as pd
import requests
import altair as alt
import streamlit as st
import requests

st.title('仮想通貨監視アプリ')

#URL設定
BASE_URL = 'https://coincheck.com'


st.sidebar.write("""
## 表示日数選択
""")
days = st.sidebar.slider('日数', 1, 10, 1)

coin = st.sidebar.selectbox(
    '仮想通貨を選択してください',
     ('BTC', 'ETH', 'NUM'))
#st.sidebar.write('You selected:', option)

act = st.sidebar.selectbox(
    '何を表示しますか？',
    ('テッィカ','全取引履歴','板情報')
)

st.title(f"""
過去{days}日間の{coin}の{act}を表示します
""")

if act == 'テッィカ':
    url = BASE_URL + '/api/ticker'
    r = requests.get(url)
    r = r.json()
if act == '全取引履歴':
    url = BASE_URL + '/api/trades'
if act == '板情報':
    url = BASE_URL + 'api/order_books'


st.write(r)




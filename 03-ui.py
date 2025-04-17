import streamlit as st 
import pandas as pd 
from datetime import datetime as dt 
button = st.button('버튼을 눌러보세요')

if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')
    
dataframe = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Join Date": [dt(2020, 1, 1), dt(2021, 2, 15), dt(2022, 5, 10), dt(2023, 8, 21)]
})

st.download_button(
    label='CSV로 다운로드',
    data = dataframe.to_csv(),
    file_name='sample.csv',
    mime='text/csv'
)

agree= st.checkbox('동의 하십니까?')

if agree:
    st.write('동의 해주셔서 감사합니다:100')
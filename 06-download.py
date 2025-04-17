import streamlit as st   

date = '''dafsafdsaffdsfsfsfsfsfsfsfsfsafsfsfsafaf'''

download_button = st.download_button("클릭하면 다운로드가 됩니다", data=data,
file_name="결과.txt")


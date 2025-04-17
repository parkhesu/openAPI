import streamlit as st  

col1, col2, col3 = st.columns([1, 5, 1])
 
with col1:
    st.write("왼쪽")
    st.write("왼쪽의 내용입니다.")
    
with col2:
    st.write("오른쪽")
    st.write("오른쪽의 내용입니다.")
    
with col3:
    st.write("왼쪽")
    st.write("왼쪽의 내용입니다.")
    
st.write("안녕~~~~~~~~~~ ~~~~~~~~~~~~~~ ~~~~~~~~~~~~~ 안녕")
    
    
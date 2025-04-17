import streamlit as st
import pandas as pd
import numpy as np 

st.title("데이터프레임 튜토리얼")
dataframe = pd.DataFrame({
    "first column" : [1, 2, 3, 4],
    "second column" : [10, 20, 30, 40],
})

st.dataframe(dataframe, use_container_width=False)
st.dataframe(dataframe, use_container_width=True)

# 테이블(static)은 DataFrame과는 다르게 interactive한 UI를 제공하지 않는다.
st.table(dataframe)

# 매트릭
st.metric(label="온도", value="10C", delta="1.2C")  # corrected 'lable' to 'label'
st.metric(label="삼성전자", value="61.000원", delta="-1,200원")  # corrected 'lable' to 'label'

# 컬럼으로 영역을 나누어서 표기하는 경우
col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,228원", delta="-12.00원")
col2.metric(label="일본JPY(100엔엔)", value="1,228원", delta="-15.00원")
col3.metric(label="유럽연합EUR", value="1,335원", delta="-11.44원")

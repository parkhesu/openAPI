import streamlit as st
import pandas as pd
from datetime import datetime as dt, timedelta  # timedelta 추가!

# 기존 코드 유지
mbti = st.radio(
    '당신의 MBTI는 무엇입니까?',
    ("ISTJ", "ISFJ", "INFJ", "INTJ",
     "ISTP", "ISFP", "INFP", "INTP",
     "ESTP", "ESFP", "ENFP", "ENTP",
     "ESTJ", "ESFJ", "ENFJ", "ENTJ",
     "선택지없음")
)

descriptions = {
    "ISTJ": "책임감 있는 관리자",
    "ISFJ": "헌신적인 수호자",
    "INFJ": "통찰력 있는 조언자",
    "INTJ": "전략적 계획가",
    "ISTP": "냉철한 문제 해결사",
    "ISFP": "감성적인 예술가",
    "INFP": "이상적인 중재자",
    "INTP": "논리적인 사색가",
    "ESTP": "모험적인 활동가",
    "ESFP": "자유로운 엔터테이너",
    "ENFP": "열정적인 탐험가",
    "ENTP": "도전적인 논쟁가",
    "ESTJ": "현실적인 지도자",
    "ESFJ": "사교적인 조정자",
    "ENFJ": "카리스마 있는 지도자",
    "ENTJ": "대담한 개혁가"
}

if mbti in descriptions:
    st.write(f'당신은 :blue[{descriptions[mbti]}]이시네요')
else:
    st.write('당신에 대해 :red[알고 싶어요]❕')

options = st.multiselect(
    '당신이 좋아하는 과일은 뭔가요?',
    ['망고','오렌지','사과','바나나','수박'],
    ['망고','오렌지']
)

st.write(f'당신의 선택은: :red[{options}] 입니다.')

values = st.slider(
    '👍🏻👍🏻👍🏻👍🏻범위의 값을 다음과 같이 지정할 수 있어요:sparkles:',
    0.0, 100.0, (25.0, 75.0))
st.write('선택 범위:', values)

# # ✅ 현재 날짜 및 시간 표시
# current_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
# st.write(f"🕒 현재 시간: :blue[{current_time}]")

# # ✅ 사용자가 날짜 선택 가능
# selected_date = st.date_input("📅 날짜를 선택하세요", dt.today())
# st.write(f"✅ 선택한 날짜: :green[{selected_date}]")

start_time = st.slider(
    "언제 약속을 잡는 것이 좋을까요?",
    min_value=dt(2025, 1, 1, 0, 0),
    max_value=dt(2025, 1, 7, 23, 0),
    value=dt(2025, 1, 3, 12, 0),
    step=timedelta(hours=1),  # timedelta 수정!
    format="MM/DD/YY - HH:mm"
)
st.write("선택한 약속 시간:", start_time)

title = st.text_input(
    label = '가고 싶은 여행지가 있나요?',
    placeholder='여행지를 입력해 주세요'
)
st.write(f'당신이 선택한 여행지:  :violet[{title}]')

number = st.number_input(
    label='나이를 입력해 주세요.',
    min_value=10,
    max_value=100,
    value=30,
    step=1
)
st.write(f'당신이 입력한 나이는:  :violet[{number}]')
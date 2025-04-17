import streamlit as st
import random
import datetime

st.title(':sparkles: 로또 생성기 :sparkles:')

def generate_lotto():
    lotto = set()
    while len(lotto) < 6:
        number = random.randint(1, 45)  # 1~45까지 랜덤 번호 생성
        lotto.add(number)
    return sorted(lotto)  # 정렬된 리스트 반환

button = st.button('로또를 생성해 주세요!')

if button:
    for i in range(1,6):
        st.subheader(f'{i}, 행운의 번호:  :green[{generate_lotto()}]')
        st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

# # 현재 날짜 표시
# current_date = datetime.datetime.now().strftime("%Y-%m-%d")
# st.write(f'오늘의 날짜: :blue[{current_date}]')

# # 버튼 클릭 시 로또 번호 생성
# if st.button('로또 번호 생성하기 🎰'):
#     lotto_numbers = generate_lotto()
#     st.write(f'🎉 당신의 로또 번호: :red[{lotto_numbers}] 🎉')
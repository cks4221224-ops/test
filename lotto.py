import streamlit as st
import random as rd
from datetime import datetime as dt
st.title("로또 번호 생성기")
st.subheader("행운의 로또 번호를 생성해드립니다!")
def generate_lotto_numbers():
    lotto=set
    while len(lotto)<6:
        number=rd.randint(1,45)
        lotto.add(number)
    return sorted(lotto)
if st.button("로또 번호 생성"):
    numbers=generate_lotto_numbers()
    st.success(f"당신의 행운의 로또 번호는: {numbers}")
    st.balloons()
print(f'생성된 시각: {dt.now().strftime("%Y-%m-%d %H:%M:%S")}')
st.write(f'생성된 시각: {dt.now().strftime("%Y-%m-%d %H:%M:%S")}')


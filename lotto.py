import streamlit as st
import random as rd
from datetime import datetime as dt

st.title("🎱 로또 번호 생성기")
st.subheader("행운의 로또 번호를 생성해드립니다!")

def generate_lotto_numbers():
    # 수정: set -> set() (괄호를 붙여야 빈 집합이 생성됩니다)
    lotto = set() 
    while len(lotto) < 6:
        number = rd.randint(1, 45)
        lotto.add(number)
    return sorted(list(lotto)) # 정렬을 위해 리스트로 변환 후 정렬

if st.button("로또 번호 생성"):
    numbers = generate_lotto_numbers()
    
    # 결과 출력
    st.success(f"당신의 행운의 로또 번호는: {numbers}")
    st.balloons()
    
    # 생성된 시각을 버튼을 눌렀을 때만 표시하도록 안으로 이동했습니다.
    current_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(f'생성된 시각: {current_time}')
    
    # 터미널 로그용 (선택 사항)
    print(f'생성된 시각: {current_time}')
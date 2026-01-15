import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime as dt 
import datetime as dT

st.title("이거슨타이틀이다이")
st.subheader("이거슨서브헤더이다이")
st.badge("Home", color="blue")
st.caption("이거슨캡션이다이")
st.text("이거슨텍스트이다이")

sample_code='''
def greet():
    print("Hello, World!")'''

st.code(sample_code, language='python')
#마크 다운 문법 지원
st.markdown('텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼드체를 설정할 수 있다')
st.markdown(':green[$\\sqrt{X^2+Y^2}=1$]와 같은 수학식도 표현 가능하다')
st.latex(r'\sqrt{X^2+Y^2=1}')

st.title("데이터프레임 출력 예시")
dataframe = pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40],
})


#메트릭
st.metric(label="온도", value="25 °C", delta="1.2 °C")
st.metric(label='삼성전자', value='140,000', delta='3,800')

#dataframe 생성
st.dataframe(dataframe)
st.table(dataframe)

#컬럼으로 영역 나누기
col1, col2, col3 = st.columns(3)
col1.metric(label='달러', value='1471원', delta='30원')
col1.metric(label='유로', value='1623원', delta='15원')
col2.metric(label='엔', value='10.5원', delta='0.3원')
col2.metric(label='위안', value='210원', delta='5원')
col3.metric(label='금', value='65,000원', delta='1,200원')
col3.metric(label='은', value='800원', delta='20원')

#버튼 클릭

button_clicked = st.button("버튼을 눌러보세요")
if button_clicked:
    st.write("버튼이 눌렸습니다!👍👍")

agreement = st.checkbox("동의하십니까?")
if agreement:
    st.write("동의하셨습니다!✅")   
else:
    st.write("동의하지 않으셨습니다.❌")

mbti = st.radio("당신의 MBTI는?", 
                ('INTJ', 'ENFP', 'ISTP', 'ESFJ'),
                index=2
                )
#라디오 단추는 한 번에 하나의 항목만 선택할 수 있음
st.write("당신의 MBTI는", mbti, "입니다.")

if mbti == 'INTJ':
    st.write("당신은 전략가형입니다.")
elif mbti == 'ENFP':
    st.write("당신은 활동가형입니다.")
elif mbti == 'ISTP':
    st.write("당신은 장인형입니다.")
else:
    st.write("당신은 사교형입니다.")

#셀렉트박스
favorite_color = st.selectbox(
    "당신이 가장 좋아하는 색깔은?",
    ('빨강', '파랑', '초록', '노랑', '보라')
)

st.write("당신이 가장 좋아하는 색깔은", favorite_color, "입니다.")

#멀티셀렉트박스
hobbies = st.multiselect(
    "당신의 취미는 무엇입니까?",
    ['독서', '여행', '운동', '요리', '게임']
)
st.write("당신의 취미는", ', '.join(hobbies), "입니다.")

#슬라이더
age = st.slider("당신의 나이는?", 0, 100, 25)
st.write("당신의 나이는", age, "살입니다.")

value = st.slider(
    '범위의 값을 다음과 같은 값으로 설정하세요',
    0.0, 100.0, (25.0, 75.0)
)

#날짜 선택
start_time = st.slider(
    '언제 약속을 잡을까요?',
    min_value=dt(2024, 1, 1, 9, 30),
    max_value=dt(2026, 12, 31, 9, 30),
    value=dt(2024, 6, 1, 12, 0),
    step=dT.timedelta(hours=30),
    format='YYYY-MM-DD HH:mm'
)
st.write('약속 시간은', start_time, '입니다.')
st.write('선택한 범위는', value, '입니다.')

#텍스트 입력
title=st.text_input(
    '가장 가고 싶은 여행지는?',
)
st.write('당신이 가장 가고 싶은 여행지는', title, '입니다.')

# 파일다운로드 버튼
st.download_button(
    label="CSV 파일 다운로드",
    data=dataframe.to_csv(index=False).encode('utf-8'),
    file_name='dataframe.csv',
    mime='text/csv',
)


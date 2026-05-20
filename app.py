import streamlit as st
st.title('천안오성고 화이팅')
st.write('연애하고 싶다!')
import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="연애 앱",
    page_icon="❤️",
    layout="centered"
)

# 제목
st.title("❤️ 두근두근 연애 앱")
st.write("이름을 입력하고 연애 궁합을 확인해보세요!")

# 입력
name1 = st.text_input("당신의 이름")
name2 = st.text_input("상대 이름")

# 버튼
if st.button("궁합 보기"):
    
    # 입력 체크
    if not name1 or not name2:
        st.warning("이름 두 개를 모두 입력해주세요!")
    
    else:
        # 랜덤 점수 생성
        score = random.randint(50, 100)

        # 결과 메시지
        if score >= 90:
            result = "천생연분 ❤️"
        elif score >= 75:
            result = "잘 어울리는 커플 😊"
        elif score >= 60:
            result = "조금 더 알아가보세요 🙂"
        else:
            result = "친구가 더 잘 어울릴 수도 😅"

        # 출력
        st.success(f"{name1} ❤️ {name2}")
        st.metric("궁합 점수", f"{score}%")
        st.write(result)

# 하단 문구
st.caption("Made with Streamlit")

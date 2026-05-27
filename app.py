import streamlit as st
from google import genai
from google.genai import types

# 페이지 설정
st.set_page_config(
    page_title="연애상담 챗봇",
    page_icon="💌"
)

st.title("💌 연애상담 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반 AI 상담")

# Secrets에서 API 키 불러오기
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except Exception:
    st.error("❌ Secrets에 GOOGLE_API_KEY를 설정해주세요.")
    st.stop()

# Gemini 클라이언트 생성
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"❌ Gemini 연결 실패: {e}")
    st.stop()

# 채팅 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요 😊 연애 고민을 편하게 이야기해주세요!"
        }
    ]

# 이전 채팅 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
prompt = st.chat_input("메시지를 입력하세요...")

if prompt:

    # 사용자 메시지 저장
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini 형식으로 변환
    history = []

    for msg in st.session_state.messages:

        role = "model" if msg["role"] == "assistant" else "user"

        history.append(
            types.Content(
                role=role,
                parts=[types.Part(text=msg["content"])]
            )
        )

    # AI 응답 생성
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=history
        )

        reply = response.text

    except Exception as e:
        reply = f"❌ 오류 발생: {e}"

    # 응답 저장
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    # 응답 출력
    with st.chat_message("assistant"):
        st.markdown(reply)

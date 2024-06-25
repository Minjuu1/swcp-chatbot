# %%writefile app.py

# 첨부 파일
# 1) create_prompt.py
# 2) create_shots.py
# 3) chat_init.py
# 4) chat_options.py

import streamlit as st
from langchain.prompts import PromptTemplate
from openai import OpenAI

import create_prompt
import create_shots
import chat_init
import chat_options

# Open AI API Key 불러오기
file_path = "/content/gdrive/My Drive/Colab Notebooks/ChatGPT/"
file = open(file_path + "OPENAI_API_KEY.txt", "r")
openai_key = file.read()
file.close()
client = OpenAI(api_key=openai_key)


# 👩‍💻 챗봇 시작 👩‍💻
chat_init.config()

# 1️⃣ 사전 정보 입력 ==============================================================================
col1, col2 =  st.columns(2)
info = {}

# 유저 정보
with col1: 
    info["user_name"] = st.text_input("이름이 무엇인가요?", key = "user_name")
    info["user_emoji"] = st.selectbox("본인의 이모지를 선택하세요:", chat_options.emojis, key="user_emoji")

# 친구 정보(== 챗봇 == 대화 상대)
with col2:
    info["bot_name"] = st.text_input("대화를 나눌 친구의 이름은 무엇인가요?", key = "bot_name")
    info["bot_emoji"] = st.selectbox("친구의 이모지를 선택하세요:", chat_options.emojis, key="bot_emoji")

# 상황 정보 입력
situation = st.selectbox("상황을 골라볼까요?: ", list(chat_options.situations.keys()), key = "situation")
info["situation"] = chat_options.prompt_situations[chat_options.situations[situation]]

# 2️⃣ 챗봇 초기 설정 ==============================================================================
# 채팅 초기화
chat_init.default()

# 프롬프트 제작
system_prompt = create_prompt.systemPrompt(info["user_name"], info["bot_name"], info["situation"])
# 시스템 프롬프트 저장
st.session_state.messages.append({"role": "system", "content": system_prompt})



# 3️⃣ 채팅 시작 ==============================================================================

st.subheader("🙋‍♀️ 역할극 시작해볼까요?")
# 역할놀이 상황에 대한 재안내
st.write(create_prompt.userPrompt(situation))

# 채팅 기록 시각화
for message in st.session_state.messages:
    if(message["role"] == "user"):
        with st.chat_message(info["user_name"], avatar=info["user_emoji"]):
            st.markdown(message["content"])
    elif(message["role"] == "assistant"):
        with st.chat_message(info["bot_name"], avatar=info["bot_emoji"]):
            st.markdown(message["content"])

# 유저의 메시지 입력받기
if user_input := st.chat_input("자유롭게 말해봅시다!"):
      # 유저 메시지 저장
      st.session_state.messages.append({"role": "user", "content": user_input})
      # 유저 메시지 출력
      with st.chat_message(info["user_name"], avatar=info["user_emoji"]):
          st.markdown(user_input)

      with st.chat_message(info["bot_name"], avatar=info["bot_emoji"]):
          # 챗봇의 답변 생성
          stream = client.chat.completions.create(
              model=st.session_state["openai_model"],
              messages=[
                  {"role": m["role"], "content": m["content"]}
                  for m in st.session_state.messages
              ],
              temperature=0.7,
              max_tokens=100,
              frequency_penalty=0.7,
              stream=True,
          )
          response = st.write_stream(stream)
      # 챗봇 답변 저장
      st.session_state.messages.append({"role": "assistant", "content": response})

# 리셋 버튼을 통해 메시지 기록 초기화
if st.button(label="⚡ Reset"):
    st.session_state["check_reset"] = True
    st.session_state.messages = []

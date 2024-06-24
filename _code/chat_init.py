import streamlit as st

import os
import base64
from langchain.prompts import PromptTemplate

from openai import OpenAI

# 웹페이지 기본 정보 세팅 함수
def header():
    st.set_page_config(
    page_title="사회성 대화 연습 챗봇",
    page_icon='💬',
    layout='wide'
    )

    st.header("🤖 대화를 연습해보자! 🤖")

# 채팅 초기화 함수
def default():
    # 리셋 버튼 활성화
    if "check_reset" not in st.session_state:
        st.session_state["check_reset"] = False
    # gpt 모델 설정
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4"
    # 메시지 저장소 활성화
    if "messages" not in st.session_state:
        st.session_state.messages = []    


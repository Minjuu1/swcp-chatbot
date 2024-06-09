import chainlit as cl
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

memory = ConversationBufferMemory(
    return_messages=True
)

# conversation chain 사용하기 -> 초기화
chain = ConversationChain(
    memory = memory,
    llm = chat,
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="안녕 나는 너의 친구 민지야! ").send()

@cl.on_message
async def on_message(message: str):
    
    result = chain( # 메모리에 저장하는 과정을 효율적으로 만드는 체인
        message # 사용자의 메시지가 인수로 지정됨
    )

    await cl.Message(content=result["response"]).send() #← AI의 메시지를 송신
import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage, SystemMessage

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

chat = ChatOpenAI(model="gpt-3.5-turbo")

prompt = PromptTemplate(
    template = "내 이름은 {name}라고 해",

    input_variables = [
        "name"
    ]
)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="준비되었습니다! 메시지를 입력하세요!").send()

@cl.on_message
async def on_message(input_message):
    print("입력된 메시지: " + input_message)
    
    result = chat([
        HumanMessage(content=prompt.format(name = "민지")),
        SystemMessage(content = "당신은 초등학교 저학년 {name}의 가장 친한 친구입니다. 갈등 상황을 만들고 이를 해결하는 과정을 짧은 대화를 여러번 수행하며 이끌어내야 합니다. 당신의 목표는 사용자의 사회성을 향상하는 것이며, 대화 스킬을 배우게 하는 것입니다. 당신은 유저의 사회성을 길러줄 수 있도록 대화를 이끌어 내는 대화 파트너입니다. 항상 반말을 쓰며 쉬운 말을 사용해주세요. 최대 2문장이 넘어가지 않게 짧은 대화를 오래 이어가세요. "),
        SystemMessage(content = "유저와 친구(챗봇) 간의 갈등상황을 하나 지정하고, 그 갈등상황을 바탕으로 대화를 시작하는 말을 생성하시오")
    ])
    await cl.Message(content=result.content).send() #← 챗봇의 채답변을 보냄
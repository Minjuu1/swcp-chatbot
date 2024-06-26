from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage

# 클라이언트 만들고 chat에 저장
chat = ChatOpenAI(
    model = "gpt-3.5-turbo"
)

result = chat(
    [

        SystemMessage(content = "당신은 {유저}의 가장 친한 친구입니다. 당신은 유저의 사회성을 길러줄 수 있도록 대화를 이끌어 내는 대화 파트너입니다. 항상 반말을 쓰며 쉬운 말을 사용해주세요. 최대 2문장이 넘어가지 않게 짧은 대화를 오래 이어가세요."),
        HumanMessage(content = "안녕! 너 왜 어제 먼저 갔어?"),
    ]
)

print(result.content)
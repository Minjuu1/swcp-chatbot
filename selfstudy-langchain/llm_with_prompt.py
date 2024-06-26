from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain import PromptTemplate

chat = ChatOpenAI(
    model = "gpt-3.5-turbo"
)

prompt = PromptTemplate(
    template = "내 이름은 {name}라고 해",

    input_variables = [
        "name"
    ]
)

result = chat(
    [
        # PromptTemplate 사용하기
        HumanMessage(content=prompt.format(name = "민지")),
        SystemMessage(content = "당신은 초등학교 저학년 {name}의 가장 친한 친구입니다. 갈등 상황을 만들고 이를 해결하는 과정을 짧은 대화를 여러번 수행하며 이끌어내야 합니다. 당신의 목표는 사용자의 사회성을 향상하는 것이며, 대화 스킬을 배우게 하는 것입니다. 당신은 유저의 사회성을 길러줄 수 있도록 대화를 이끌어 내는 대화 파트너입니다. 항상 반말을 쓰며 쉬운 말을 사용해주세요. 최대 2문장이 넘어가지 않게 짧은 대화를 오래 이어가세요. "),
    ]
)

print(result.content)
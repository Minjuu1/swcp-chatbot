from tkinter.filedialog import Open
from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {
        "input": "나는 그 별명이 싫은데 너가 자꾸 말해서 속상해",
        "output": "그랬구나 나는 너도 재밌어하는 줄 알았어. 미안해"
    }
]

prompt = PromptTemplate(
    input_variables=["input", "output"],
    template = "사용자: {input}\n챗봇(친구): {output}",
)

fewshot_prompt = FewShotPromptTemplate(
    examples = examples,
    example_prompt = prompt,
    # 지시어 추가하기
    prefix = "초등학교 친구들의 대화입니다",
    suffix = "입력: {input_string}",
    # few shot prompt template 입력변수 설정
    input_variables = ["input_string"],
)

llm = OpenAI()

formatted_prompt = fewshot_prompt.format(
    input_string = "너 숙제 다 했어?"
)

result = llm.predict(formatted_prompt)
print("formatted_prompt: ", formatted_prompt)
print("result: ", result)
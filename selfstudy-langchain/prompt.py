from langchain import PromptTemplate

prompt = PromptTemplate(
    template = "내 이름은 {name}라고 해",

    input_variables = [
        "name"
    ]
)

# JSON 파일로 템플릿 저장하기
prompt_json = prompt.save("prompt.json")

# 파일 읽어들여 사용하기
# from langchain.prompts import load_prompt
# loaded_prompt = load_prompt("prompt.json")
# print(loaded_prompt.format(name = "민지"))
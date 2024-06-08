from langchain import PromptTemplate

prompt = PromptTemplate(
    template = "내 이름은 {name}라고 해",

    input_variables = [
        "name"
    ]
)

print(prompt.format(name = "민지"))
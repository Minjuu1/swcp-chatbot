# LangChain

## 추가하면 좋을 것 같은 chain

- OpenAIModerationChain
    open ai의 정책에 준수하는지 확인하는 기능
    폭력, 차별, 자해 등의 문제 있는 콘텐츠 생성을 방지하기 위함
    자유로운 대화 기능의 한계인 폭력적인/부정적인 콘텐츠를 막기 위해 추가 예정

- 대화를 마무리하는 chain?
    예시)
    write_article_chain = LLMChain(
        llm = chat,
        prompt = PromptTemplate(
            # 해당 체인의 기능을 템플릿에 미리 설정
            template="{input}에 관한 기사를 써주세요",
            input_variables = ["input"],
        )
    )

    result = write_article_chain.run("input message")

## 공식 문서
   https://python.langchain.com/

   https://blog.langchain.dev/

   https://github.com/kyrolabs/awesome-langchain   
    - 오픈소스 프로젝트, 라이브러리, 튜토리얼 등

   
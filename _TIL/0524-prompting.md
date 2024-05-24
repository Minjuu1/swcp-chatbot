# Prompting Engineering

## How to make Prompt
### 프롬프트 가이드 라인
- 과업의 배경 설명 
    e.g. 당신은 번역기입니다
- 과업의 결과 예시 설명: **JSON 포맷**
    e.g. 출력 결과: {{"step 1: <입력텍스트>, "step 2": <true/false>, "step 3": <번역 결과>}}
- 단계별 가이드 알려주기
    e.g.  STEP 별로 작업을 수행하면서 그 결과를 아래의 출력 결과 JSON 포맷에 저장하세요.
    step 1. 아래 텍스트를 읽어올 것 ..
- 제약사항 설명하기
    e.g. 입력값이 영어가 아니라면 진행을 멈출 것
- 적절한 구분자 사용
    1. '''{text}''': 백틱, 단락 구분용
    2. <키워드>내용<키워드/>: xml tag, 내용물 구분용
    3. JSON: 내용물 구분용
    -> 일관되게 사용하는 것이 중요

## Few-shot Prompting

아래 예시를 참조해 대화를 이어나가주세요.
'''
user: 대화예시1
bot: 대화예시1
'''
user: 대화예시2
bot: 대화예시2
'''

## JSON 모드

response_format={ "type": "json_object" }
사용자 메시지에도 json으로 기술하라는 문구가 반드시 들어가야 한다

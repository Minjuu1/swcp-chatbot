# Assistants API

## Assistant API 콘셉

1. 자율적 에이전트
- 자동으로 도구를 사용하여 최적의 응답 생성해줌
    - 프로그램 실행하는 **코드 인터프리터**
    - 업로드한 파일 내용 탐색하는 **지식 검색**
    - **Function Calling**(사용자 정의 함수와 연동)

2. 영구적 대화 세션 관리 기능
- 대화 내용을 오픈 AI가 관리하며 대화에 적용
- 벡터 DB, NoSQL 등을 생략 가능 -> **가벼운 프로그램**

3. 데이터 관리 프로세스
- 오픈AI 내부적으로 데이터 관리 체계 구축
- API 객체와 기능
    - Assistant: 챗봇 하나에 대응되는 객체
    - Thread: 대화 세션 / 하나의 thread 당 하나의 대화 컨텍스트
        - Message: 사용자 메시지 및 Assistant의 응답 메시지
        - Run: 현재까지 쌓인 메시지를 입력값으로 하여 답변 생성 (상태값 지님 ex. in_progress, completed)
        - Run Detail: run에 대한 세부 정보
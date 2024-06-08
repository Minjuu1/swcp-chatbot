import json
import openai

# 채팅 결과가 response 변수에 저장
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "user",
            "content": "초등학생에게 필요한 지식은 무엇이 있을까?"
        },
    ],
    # 문장의 최대 토큰 수
    max_tokens = 100,
    # 다양성 나타내는 매개변수 (0~2)
    temperature = 1,
    # 생성할 문장 수 - index 매겨진 결과 출력
    n = 2
)

print(json.dumps(response, indent = 2, ensure_ascii=False))
# dumps = 보기좋게 답변을 변환하는 함수



# 결과값
# object = API가 반환한 객체 종류
# choices = message의 content에 답변 있음 / role = assistant
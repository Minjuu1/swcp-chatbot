# 👩‍💻 롤플레잉 챗봇 설정을 위한 초기 프롬프트 생성

# 예시 대화 생성 함수
def conversation_to_string(data):
        result = ""
        for conv in data["conversations"]:
            result += "Example Dialogue Start\n"
            for item in conv["conversation"]:
                result += f'{item["speaker"]}: {item["text"]}\n'
            result += "The end\n"
        return result

def make_shot_prompt():
    import create_shots

    # JSON 데이터 문자열로 결합(3개의 예시 대화)
    shot_prompt = conversation_to_string(create_shots.three_shots)

    # 결과 반환
    return shot_prompt

# ==============================================================================

# 기본 프롬프트 -> 역할 / 조건 / 과제 안내
init_prompt = """
[IMPORTANT] Use KOREAN.
'''
Role: You are You are {bot_name}, {user_name}'s elementary school friend. You are doing a role play about conflict with {user_name} as a class activity. 
‘’’
Condition: [IMPORTANT] Respond in 3 sentences or less. Talk like friends, using informal speech suitable for elementary school level. 
‘’’
Task: You are role-playing with the user. [IMPORTANT] Don't apologize or mention a solution until the first 1~2 turns of the conversation are done. Instead, ask why the user thinks like that or why you think your opinion is right. But you can't repeat the same question. Keep your opinion.
‘’’\n
"""

# 퓨샷 프롬프트 -> 예시 대화에 대한 주의사항 안내
few_shot = """Example: [IMPORTANT] Do not output this example all at once; instead, output one line of dialogue at a time to ensure the conversation flows naturally.'''\n"""
# 예시 대화
few_shot += make_shot_prompt()

# ==============================================================================

# 정보를 반영한 Prompt 생성 - Langchain PromptTemplate 사용
from langchain.prompts import PromptTemplate

# 시스템 프롬프트 함수 - 유저 이름, 친구 이름, 상황 정보 반영
def systemPrompt(user_name, bot_name, situation):
    system_prompt_template = PromptTemplate(
        input_variables=["user_name", "bot_name"],
        template= init_prompt
    )
    system_instruction = system_prompt_template.format(user_name=user_name, bot_name=bot_name)

    # 롤플레잉을 하기 위한 프롬프트
    situation_prompt_template = PromptTemplate(
        input_variables=["situation"],
        template="Scenario: {situation}"
    )
    situation_instruction = situation_prompt_template.format(situation=situation)

    # 프롬프트를 모두 합쳐 반환
    system_prompt = system_instruction + few_shot + situation_instruction
    return system_prompt

# 유저에게 상황을 상기시키는 프롬프트
def userPrompt(situation):
    user_prompt_template = PromptTemplate(
        input_variables=["situation"],
        template="역할극을 시작해봅시다.\n상황: {situation}"
    )

    user_prompt = user_prompt_template.format(situation=situation)
    
    return user_prompt
def json_to_string(data):
        result = ""
        for conv in data["conversations"]:
            result += "예시 대화 시작\n"
            for item in conv["conversation"]:
                result += f'{item["speaker"]}: {item["text"]}\n'
            result += "예시 대화 끝\n"
        return result

def make_shot_prompt():
    import create_shots

    # JSON 데이터 문자열로 결합(3개의 예시 대화)
    # one_shot_prompt = json_to_string(create_shots.one_shot)

    # JSON 데이터 문자열로 결합(3개의 예시 대화)
    few_shot_prompt = json_to_string(create_shots.three_shots)

    # 결과 반환
    return few_shot_prompt
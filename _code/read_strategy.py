def strategy_to_string(data):
    result = ""
    for strategy in data["strategy"]:
        for item in strategy["strategy"]:
            result += f'category: {item["category"]} - 전략: {item["전략"]} / 표현: {item["표현"]}\n'
        result += "'''\n"
    return result

def make_strategy_prompt():
    import create_strategy

    # JSON 데이터 문자열 결합
    strategy_prompt = strategy_to_string(create_strategy.strategies)

    # 결과 반환
    return strategy_prompt
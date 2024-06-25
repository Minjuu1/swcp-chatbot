emojis = ["😀", "🙂", "😎", "😉", "😛", "😂", "🐶", "🐱", "🐭", "🐰", "🐻", "🐹"]

# 갈등 상황 옵션
# 물건 소유권에 대한 갈등, 거절할 때의 갈등, 의견이 맞지 않아 일어나는 갈등, 언어적 공격과 관련된 갈등
# 사용자에게 보이는 옵션
situations = {
    "모둠에서 한 명당 한 색깔의 볼펜을 사용할 수 있어. 근데 너랑 친구 모두 빨간색 볼펜을 갖고 싶어하네? 어떻게 할까?" : "a",
    "친구가 숙제를 베끼고 싶대. 근데 난 숙제 보여주기 싫은데..어떻게 말해야할까?" : "b",
    "사인할 때 원래 이름을 쓰는 거잖아. 근데 친구가 사인할 때 모양을 그려도 된대. 어, 친구가 틀린 거 같은데?" : "c",
    "친구가 자꾸 별명으로 놀리네. 어떻게 하지 말라고 하지?" : "d"
}

# gpt에게 프롬프트로 입력되는 옵션
prompt_situations = {
    "a": "In your group, each person can only use one color of pen. Both you and your friend want to use the red pen. You really like the color red and want to use it.", 
    "b": "You don't have much time left and you don't want to do the homework yourself, so you want to copy your friend's homework. But your friend doesn't want to show it to you. You really need to get the homework done.",
    "c": "You believe you can draw a shape when making a signiture because your mom told you so. But your friend keeps saying it's wrong. You think you're not wrong.",
    "d": "You keep teasing your friend with a nickname because her reaction is funny. It doesn't seem like she really mind. Since it's fun, you want to keep doing it."
}

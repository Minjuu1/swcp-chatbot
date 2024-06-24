
conversation1 = [
    {
        "speaker": "user",
        "text": "내 생각에는 오늘 공원에서 자전거 타는 게 좋을 것 같아."
    },
    {
        "speaker": "bot",
        "text": "음, 나는 집에서 보드게임 하는 게 더 재밌을 것 같은데. 너는 어때?"
    },
    {
        "speaker": "user",
        "text": "자전거 타는 것도 재밌겠지만, 보드게임은 좀 지루하지 않을까?"
    },
    {
        "speaker": "bot",
        "text": "아니야, 새로 산 보드게임이 있어서 해보고 싶어."
    },
    {
        "speaker": "user",
        "text": "미안한데, 난 바깥에서 노는 게 더 좋아서. 다른 건 어떨까?"
    },
    {
        "speaker": "bot",
        "text": "그러면 보드게임 조금 하고 나서 공원 가는 건 어때?"
    },
    {
        "speaker": "user",
        "text": "그건 괜찮을 것 같아. 그런데 시간이 될까?"
    },
    {
        "speaker": "bot",
        "text": "글쎄, 너도 알잖아. 보드게임 조금 하고 나면 충분히 공원 갈 시간 있을 거야."
    },
    {
        "speaker": "user",
        "text": "알겠어. 그럼 보드게임 하고 나서 바로 공원 가자."
    },
    {
        "speaker": "bot",
        "text": "좋아. 너도 알지만, 같이 시간을 보내는 게 중요하니까."
    },
    {
        "speaker": "user",
        "text": "맞아. 나도 그렇게 생각해. 그렇게 하자."
    },
    {
        "speaker": "bot",
        "text": "그럼 네 집에서 보드게임 하기로 하자. 몇 시에 갈까?"
    },
    {
        "speaker": "user",
        "text": "오후 1시에 만나는 건 어때?"
    },
    {
        "speaker": "bot",
        "text": "좋아, 그때 보자!"
    }
]

conversation2 = [
    {
        "speaker": "user",
        "text": "bot, 혹시 네 색연필 좀 빌려줄 수 있어?"
    },
    {
        "speaker": "bot",
        "text": "왜 필요해?"
    },
    {
        "speaker": "user",
        "text": "어제 그림 숙제를 못 해서 오늘 급하게 해야 할 것 같아서."
    },
    {
        "speaker": "bot",
        "text": "음, 그런데 나도 지금 색칠해야 하는데..."
    },
    {
        "speaker": "user",
        "text": "그럼 내가 10분 정도만 빌려가도 될까? 금방 돌려줄게."
    },
    {
        "speaker": "bot",
        "text": "그래, 10분 정도면 괜찮을 것 같아."
    },
    {
        "speaker": "user",
        "text": "고마워, bot! 덕분에 오늘 숙제 낼 수 있겠다."
    },
    {
        "speaker": "bot",
        "text": "근데 user, 다음에는 색연필을 미리 챙기는 게 좋을 것 같아. 나도 곤란할 때가 있어."
    },
    {
        "speaker": "user",
        "text": "맞아, 미안해. 다음엔 꼭 챙길게."
    },
    {
        "speaker": "bot",
        "text": "괜찮아, 알았으면 됐어."
    },
    {
        "speaker": "user",
        "text": "그래도 빌려줘서 정말 고마워. 너 덕분에 큰일 날 뻔했어."
    },
    {
        "speaker": "bot",
        "text": "별말을 다해. 우리가 서로 도울 수 있으면 좋은 거지."
    },
    {
        "speaker": "user",
        "text": "맞아, 다음에 내가 도와줄 일이 있으면 꼭 말해줘."
    }
]


# 각 데이터 비교를 위해 예시 대화 1개를 담은 json 변수, 대화 3개를 담은 변수 생성
# 1개의 대화
one_shot = conversation1


# 세 개의 대화 결합
three_shots = {
   "conversations": [
       {"conversation": conversation1},
       {"conversation": conversation2}
   ]
}

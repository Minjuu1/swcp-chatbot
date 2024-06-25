
conversation1 = [
    {
        "speaker": "user",
        "text": "오늘 오후 자전거 타러 가는 거 어때?"
    },
    {
        "speaker": "bot",
        "text": "음, 나는 놀이터에서 놀고싶은데. 왜 자전거 타고 싶어?"
    },
    {
        "speaker": "user",
        "text": "나 어제부터 자전거 타고 싶었거든. 같이 달리면 재밌지 않을까?"
    },
    {
        "speaker": "bot",
        "text": "글쎄.. 나도 놀이터에서 하고 싶은 놀이가 있어서.."
    },
    {
        "speaker": "user",
        "text": "그럼 이건 어떨까? 놀이터에서 놀다가 자전거도 타러 가는거지!"
    },
    {
        "speaker": "bot",
        "text": "좋은데? 나 놀이터에서 술래잡기 하고 싶은데 넌 어때?"
    },
    {
        "speaker": "user",
        "text": "미안한데, 내가 달리기는 하기 싫어. 모래놀이 하는거 어때?"
    },
    {
        "speaker": "bot",
        "text": "좋아 그럼! 놀이터에서 놀고 자전거 타러 가자"
    },
    {
        "speaker": "user",
        "text": "그래, 몇 시에 만날까? 3시 어때?"
    },
    {
        "speaker": "bot",
        "text": "좋아. 그럼 그때 보자!"
    }
]

conversation2 = [
    {
        "speaker": "user",
        "text": "나도 게임에 끼워줄 수 있어? 게임 하고 싶은데.."
    },
    {
        "speaker": "bot",
        "text": "안돼 우리 지금 한창 하고 있어. 왜 이제 와?"
    },
    {
        "speaker": "user",
        "text": "미안해 어제 못한 숙제가 있었어서 그거 하다가 늦었어"
    },
    {
        "speaker": "bot",
        "text": "음, 근데 다음 판 같이 해도 돼?"
    },
    {
        "speaker": "user",
        "text": "다음에는 나 꼭 끼워주는거지? 나 너무 하고 싶어."
    },
    {
        "speaker": "bot",
        "text": "그럼, 이번 판은 너 끼워주면 규칙이 헷갈릴 거 같아"
    },
    {
        "speaker": "user",
        "text": "알겠어. 내가 조금 급했지. 미안해"
    },
    {
        "speaker": "bot",
        "text": "아니야 같이 놀면 좋은걸 뭐~ 조금만 기다려줘"
    },
    {
        "speaker": "user",
        "text": "고마워! 옆에 앉아서 잠깐 보고 있을게"
    },
    {
        "speaker": "bot",
        "text": "그래. 얼른 끝낼게!"
    }
]

conversation3 = [
    {
        "speaker": "user",
        "text": "나도 이 책 읽고 싶은데.. 내가 읽어도 될까?"
    },
    {
        "speaker": "bot",
        "text": "음 나도 이거 진짜 읽고 싶어. 이 책 읽고 싶은 이유가 있어?"
    },
    {
        "speaker": "user",
        "text": "왜냐하면 내가 이 주인공 돼지 진짜 좋아하거든. 다음 이야기 알고 싶어서"
    },
    {
        "speaker": "bot",
        "text": "그렇구나 근데 나도 이 편을 진짜 읽고 싶었거든 어떡하지?"
    },
    {
        "speaker": "user",
        "text": "내가 진짜 빨리 읽을 수 있는데. 너만 괜찮으면 내가 먼저 읽어도 될까?"
    },
    {
        "speaker": "bot",
        "text": "너가 먼저 읽는다고? 그건 안될 것 같은데.. 내가 먼저 읽고 싶어."
    },
    {
        "speaker": "user",
        "text": "그럼 어쩔 수 없지. 너가 먼저 읽고 다음에 내가 빌릴게."
    },
    {
        "speaker": "bot",
        "text": "양보해줘서 고마워. 내가 빨리 읽고 줄게."
    },
    {
        "speaker": "user",
        "text": "알겠어. 대신 읽고 바로 나한테 줘야 해?"
    },
    {
        "speaker": "bot",
        "text": "그래. 너한테 바로 줄게! 약속해."
    }
]

# 각 데이터 비교를 위해 예시 대화 1개를 담은 json 변수, 대화 3개를 담은 변수 생성
# 1개의 대화
one_shot = conversation1


# 세 개의 대화 결합
three_shots = {
   "conversations": [
       {"conversation": conversation1},
       {"conversation": conversation2},
       {"conversation": conversation3}
   ]
}

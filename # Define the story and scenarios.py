# Define the story and scenarios
story = {
    "start": {
        "description": "당신은 우주선을 타고 성간 택배를 배달하는 우주 택배원입니다.\n별과 별 사이를 누비며 사람들이 필요한 물건을 갖다 주는 보람찬 일이죠.\n여느 때와 같던 어느 날, 당신은 퇴근 후 녹초가 된 몸을 이끌고 우주선으로 돌아와 깜빡 잠들었다 깨어납니다.",
        "choices": {
            "1": "눈을 뜬다.",
        },
        "next": {
            "1": "look_around",
        },
         "image": "forest.jpg"
    },
    "look_around": {
        "description": "잠시 낮잠을 잔 것 뿐이니 분명히 당신의 우주선 안이어야 할 텐데, 뭔가 이상합니다.",
        "choices": {
            "1": "아래를 쳐다본다.",
            "2": "위를 쳐다본다."
        },
        "next": {
            "1": "look_down",
            "2": "look_up"
        }
    },
    "look_down": {
        "description": "확실히 뭔가 이상합니다.\n오래되어서 낡고 헤져 있어야 할 조종석 팔걸이는 이제 광이 나는 새것으로 변해 있네요.\n누가 당신이 잠든 사이에 조종석을 통째로 뜯어서 바꿔 두기라도 한 게 아니라면 이곳은 확실히 당신의 우주선이 아닌 것 같네요.",
        "choices": {
            "1": "일어서서 방 안을 더 둘러 본다.",
            "2": "주변을 더 둘러 본다."
        },
        "next": {
            "1": "fight_animal",
            "2": "run_away"
        }
    },
    "look_up": {
        "description": "You meet a villager who offers help. What do you want to do?",
        "choices": {
            "1": "Accept help",
            "2": "Decline help"
        },
        "next": {
            "1": "accept_help",
            "2": "decline_help"
        }
    },
    "fight_animal": {
        "description": "You fought bravely but the animal overpowered you. Game over.",
        "choices": {},
        "next": {}
    },
    "run_away": {
        "description": "You managed to escape safely. What do you want to do next?",
        "choices": {
            "1": "Explore the forest",
            "2": "Stay put"
        },
        "next": {
            "1": "explore_forest",
            "2": "stay_put"
        }
    },
    "accept_help": {
        "description": "The villager helps you find your way out of the forest. You win!",
        "choices": {},
        "next": {}
    },
    "decline_help": {
        "description": "You decline the help and get lost in the forest. Game over.",
        "choices": {},
        "next": {}
    }
}

# Game loop
def play_game():
    current_scene = "start"
    
    while True:
        scene = story[current_scene]
        print(scene["description"])
        
        if not scene["choices"]:
            print("The end.")
            break
        
        for choice, description in scene["choices"].items():
            print(f"{choice}: {description}")
        
        player_choice = input("Enter the number of your choice: ")
        
        if player_choice in scene["next"]:
            current_scene = scene["next"][player_choice]
        else:
            print("Invalid choice. Try again.")

# Start the game
play_game()
import random

def play_game():
    print("歡迎來到猜拳遊戲！")
    print("選擇你的選項:")
    print("1. 石頭")
    print("2. 剪刀")
    print("3. 布")

    options = ["石頭", "剪刀", "布"]
    user_choice = int(input("請輸入你的選擇 (1-3): "))
    
    if user_choice not in [1, 2, 3]:
        print("請輸入有效的選擇！")
        return

    user_choice -= 1
    computer_choice = random.randint(0, 2)

    print("你選擇了：" + options[user_choice])
    print("電腦選擇了：" + options[computer_choice])

    if user_choice == computer_choice:
        print("平局！")
    elif (user_choice - computer_choice) % 3 == 1:
        print("你贏了！")
    else:
        print("你輸了！")

while True:
    play_game()
    replay = input("要再玩一次嗎？(是/否): ")
    if replay.lower() != "是":
        break
import random
from game_data import data
from art import logo
from art import vs
print(logo)

def higher_or_lower():
    should_continue = True
    current_score = 0

    remaining_data = data.copy()
    info_A01 = random.sample(data, 1)
    info_A = info_A01[0]
    remaining_data.remove(info_A)
    # 从数据中删除info_A,避免下面的info_B抽到A

    while should_continue:
        info_B01 = random.sample(remaining_data, 1)
        info_B = info_B01[0]
        # 有别与random.choice, random.sample 返回的是列表，所以需要提取列表中的元素
        print(f"Current score: {current_score}")
        print(f"Compare A: {info_A['name']}, a {info_A['description']} from {info_A['country']}. ")
        print(vs)
        print(f"Compare B: {info_B['name']}, a {info_B['description']} from {info_B['country']}. ")
        choice = input("Who has more followers? Type 'A' or 'B': \n")
        if info_A['follower_count'] > info_B['follower_count']:
            if choice == 'A':
                should_continue = True
                current_score += 1
            if choice == 'B':
                print("You are wrong, Game over!")
                again = input("play again? 'Y' or 'N'")
                if again == 'Y':
                    higher_or_lower()
                else:
                    break
        elif info_A['follower_count'] < info_B['follower_count']:
            if choice == 'B':
                should_continue = True
                current_score += 1
                info_A = info_B
            if choice == 'A':
                print("You are wrong, Game over!")
                again = input("play again? 'Y' or 'N'")
                if again == 'Y':
                    higher_or_lower()
                else:
                    break

higher_or_lower()
import random
from art import logo
from  replit import clear

print(logo)
times = 0
numbers = list(range(1, 101))

def diff():
    global times
    if DIFF == '1':
        times = 10
    elif DIFF == '2':
        times = 7
    elif DIFF == '3':
        times = 5

should_continue = True

while should_continue:
    print("Guess a number between 1 to 100")
    DIFF = input("choose a difficulty: 1.easy 2.medium 3.hard: \n")
    diff()
    the_number = random.choice(numbers)
    print(f"you have {times} times to guess")

    for i in range(times):
        guess01 = int(input("make a guess"))
        if guess01 > the_number:
            times -= 1
            print("too high")
            if times > 0:
                print(f"you have {times} times to guess")
            if times == 0:
                print("you ran over the times, game over")
                restart = input("Do you want to play again? 'y' or 'n':\n")
                if restart == 'y':
                    clear()
                    should_continue = True
                else:
                    should_continue = False
                    break

        elif guess01 < the_number:
            times -= 1
            print("too low")
            if times > 0:
                print(f"you have {times} times to guess")
            elif times == 0:
                print("you ran over the times, game over")
                restart = input("Do you want to play again? 'y' or 'n':\n")
                if restart == 'y':
                    clear()
                    should_continue = True
                else:
                    should_continue = False
                    break

        elif guess01 == the_number:
            print("That's right!")
            restart = input("Do you want to play again? 'y' or 'n':\n")
            if restart =='y':
                clear()
                # 虽然不知道为什么clear()没有清空屏幕，但是指令被清除了，成功实现重新开始游戏
                should_continue = True
            else:
                should_continue = False
                break


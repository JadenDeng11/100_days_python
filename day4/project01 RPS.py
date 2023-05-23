rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
game_images=[rock,paper,scissors]

computer_choose=random.randint(1,3)
choose=int(input('what do you choose: 1.rock 2.paper 3.scissors \n'))
if computer_choose==1:
    print(f"computer choose is rock,{game_images[computer_choose-1]}")
    if choose==1:
        print('drew')
    elif choose==2:
        print('you win!')
    else :
        print('you lost!')

elif computer_choose==2:
    print(f"computer choose is paper, {game_images[computer_choose-1]}")
    if choose==1:
        print('you lost!')
    elif choose==2:
        print('drew')
    else :
        print('you win!')

else:
    print(f"computer choose is scissors, {game_images[computer_choose-1]}")
    if choose==1:
        print('you win!')
    elif choose==2:
        print('you lost!')
    else :
        print('you win!')
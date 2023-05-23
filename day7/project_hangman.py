import random
import hangman_stages
import hangman_words

chosen_word=random.choice(hangman_words.word_list)
lives=6
end_of_game=False
# 因为不只有一种情况会导致游戏结束，所以要加一个end_of_game

display=[]
for letter in chosen_word:
    display+='_'

print('Welcome to HANGMAN!')
print(display)

while not end_of_game:
    guess = input("guess a letter: ").lower()

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
            print('you are right!keep going!')

    print(display)
    if guess not in chosen_word:
        print('you are wrong')
        lives-=1
        if lives==0:
            end_of_game=True
            print('you lose, the hangman died.')
    elif not '_' in display:
        end_of_game=True
        print('you win! the hangman survived.')

    print(hangman_stages.stages[lives])
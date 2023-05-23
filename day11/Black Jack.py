import random
from art import logo
from replit import clear
print(logo)
player_card = []
dealer_card = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
begin01 = input("type 'y' to start the game, type 'n' to exit: \n")

def card_choice():
    player_card = [random.choice(cards), random.choice(cards)]
    dealer_card = [random.choice(cards), random.choice(cards)]
    return player_card, dealer_card

def calculate_total(cards):
    total = 0
    for card in cards:
        total += card
    return total

should_continue = True

if begin01 =='y':
    player_card, dealer_card = card_choice()
    while should_continue:
        add_player = calculate_total(player_card)
        add_dealer = calculate_total(dealer_card)
        print(f"Dealer's first card:{dealer_card[0]}")
        print(f"your cards is {player_card}, your total is {add_player}")
        if add_player == 21 and not add_dealer ==21:
            print(f"you win! dealer's card is {dealer_card}")
            should_continue =False
        elif add_dealer == 21:
            print(f"you lost! dealer's card is {dealer_card}")
            should_continue =False
        else:
            if add_player > 21:
                if 11 in player_card:
                    if add_player-10 >21:
                        print(f"you win! dealer's card is {dealer_card}")
                        should_continue = False
                    else:
                        add_player = add_player - 10
                        for i in player_card:
                            if i == 11:
                                i = 1
                else:
                    print(f"you lost! dealer's card is {dealer_card}")
                    should_continue = False
            else:
                more_card = input("Do you want another card? 'y' or 'n'\n")
                if more_card == 'y':
                    player_card.append(random.choice(cards))
                    should_continue = True
                else:
                    dealer_card_continue=True
                    while dealer_card_continue:
                        add_dealer = calculate_total(dealer_card)
                        if add_dealer < 17:
                            dealer_card.append(random.choice(cards))
                            dealer_card_continue = True
                        elif add_dealer > 21:
                            print(f"you win! dealer's card is {dealer_card}")
                            dealer_card_continue=False
                            should_continue=False
                        else:
                            add_player = calculate_total(player_card)
                            if add_player < add_dealer:
                                print(f"you lost! dealer's card is {dealer_card}")
                                should_continue = False
                            elif add_player == add_dealer:
                                print(f"That's a drew, dealer's card is {dealer_card}")
                                should_continue = False
                            elif add_player > add_dealer:
                                print(f"you win! dealer's card is {dealer_card}")
                                should_continue = False
                            dealer_card_continue = False

import random
from random import sample

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
player_starting_hand = sample(cards, 2)
computer_starting_hand = sample(cards, 2)
computer_displayed_card = random.choice(computer_starting_hand)
player_current_hand = player_starting_hand
computer_current_hand = computer_starting_hand
game_on = True

print(f"Computer's starting card is: {computer_displayed_card}")
print(f"Your starting cards are: {player_starting_hand}")

def check_initial_win():
    global game_on
    if sum(player_starting_hand) == 21:
        print(f"Player deals blackjack, you win!")
        game_on = False
    elif sum(computer_starting_hand) == 21:
        print(f"Computer deals blackjack, you lose!")
        game_on = False

def check_win():
    global game_on
    if sum(player_current_hand) == 21:
        print(f"Player deals Blackjack, you win!")
        game_on = False
    elif sum(computer_current_hand) == 21:
        print(f"Computer deals Blackjack, you lose!")
        game_on = False
    else:
        pass

def check_bust():
    global game_on
    if sum(player_current_hand) > 21:
        print(f"Your current hand is {sum(player_current_hand)}")
        print(f"Player busts, you lose!")
        game_on = False
    elif sum(computer_current_hand) > 21:
        print(f"Computer's current hand is {sum(computer_current_hand)}")
        print(f"Computer busts, you win!")
        game_on = False
    else:
        pass

def player_draw_card():
    player_new_card = random.choice(cards)
    if player_new_card != 1 and player_new_card != 11:
        print(f"You drew a {player_new_card}")
        player_current_hand.append(player_new_card)
        check_win()
        check_bust()
    elif player_new_card == 1 or 11:
        pick_card = int(input(f"You drew an Ace, would you like to count it as 1 or 11?: "))
        if pick_card == 1:
            player_current_hand.append(1)
            check_win()
        elif pick_card == 11:
            player_current_hand.append(11)
            check_win()
            check_bust()

def computer_draw_card():
    while sum(computer_current_hand) < 17 and sum(computer_current_hand) < sum(player_current_hand):
        computer_new_card = random.choice(cards)
        if computer_new_card != 1 and computer_new_card != 11:
            computer_current_hand.append(computer_new_card)
            check_win()
            check_bust()
        elif computer_new_card == 1 or 11:
            if sum(computer_current_hand) + 11 > 21:
                computer_new_card = 1
                computer_current_hand.append(1)
            else:
                computer_current_hand.append(11)
    else:
        pass

def computer_trump_card():
    if sum(player_current_hand) >= sum(computer_current_hand):
        computer_new_card = random.choice(cards)
        if computer_new_card != 1 and computer_new_card != 11:
            computer_current_hand.append(computer_new_card)
            check_win()
            check_bust()
        elif computer_new_card == 1 or 11:
            if sum(computer_current_hand) + 11 > 21:
                computer_new_card = 1
                computer_current_hand.append(1)
            else:
                computer_current_hand.append(11)
    else:
        pass

def compare_hands():
    if sum(player_current_hand) > sum(computer_current_hand):
        print(f"Your hand of {sum(player_current_hand)} is bigger than computer's hand of {sum(computer_current_hand)}, you win!")
    elif sum(computer_current_hand) > sum(player_current_hand):
        print(f"Your hand of {sum(player_current_hand)} is smaller than computer's hand of {sum(computer_current_hand)}, you lose!")
    elif sum(computer_current_hand) == sum(player_current_hand):
        print(f"Your hand of {sum(player_current_hand)} is tied with computer's hand of {sum(computer_current_hand)}, it's a tie.")

def play():
    global game_on
    check_initial_win()
    while game_on:
        player_choice = input(f"Your current hand is {sum(player_current_hand)}, do you wish to hit or stay? ")
        if player_choice == 'hit':
            player_draw_card()
            computer_draw_card()
        elif player_choice == 'stay':
            computer_draw_card()
            computer_trump_card()
            if game_on:
                compare_hands()
                game_on = False

play()

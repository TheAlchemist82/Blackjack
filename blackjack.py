import random
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
computer = []
player = []

def calculation_score(players_cards, computers_cards):
    player_score = sum(players_cards)
    computer_score = sum(computers_cards)
    if player_score > computer_score:
        print("Your cards are higher than the computers, you win!")
    elif computer_score > player_score:
        print("Computers cards are higher, you lose :(")
    elif computer_score == player_score:
        print("Its a draw!")

def starting_hand(players_cards, computers_cards):
    play = False
    direction = input("Would you like to play a game of blackjack (y or n): ")
    if direction == "y":
        play = True
    else:
        print("Alright")

    players_cards += random.choices(cards, k=2)
    computers_cards += random.choices(cards, k=1)
    while play:
        print(f"    Your Cards:{players_cards}, Sum of your cards: {sum(players_cards)}\n    Computers Cards: {computers_cards}")
        hit_me_q = input("Would you like another card? (y or n): ")
        if hit_me_q == "y":
            players_cards += random.choices(cards, k=1)
            if sum(players_cards) == 21 and len(players_cards) == 2:
                return 0

            if 11 in players_cards and sum(players_cards):
                players_cards.remove(11)
                players_cards.append(1)
                print("Since you have an ace, you can turn that into a '1'.")
            elif 11 in computers_cards and sum(computers_cards):
                computers_cards.remove(11)
                computers_cards.append(1)
                print("Since the computer has an ace, it can turn that to a one")

            if sum(players_cards) > 21:
                print("You went over 21, you busted!")
                play = False
            elif sum(computers_cards) > 21:
                print("Computer went over 21, you win!")
                play = False
        else:
            computers_cards += random.choices(cards, k=1)
            print(f"    Computers final hand: {computers_cards}, Sum of computers final hand: {sum(computers_cards)}")
            calculation_score(player, computer)
            play = False

starting_hand(player, computer)

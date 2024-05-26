from art import logo
import random

def clear_console():
    """Clears the console."""
    print("\n" * 50)

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculates the score of the current deck."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, computer_score):
    """Compares the player score with the computer's score."""
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack"
    elif player_score == 0:
        return "Win with a BlackJack"
    elif player_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif player_score > computer_score:
        return "You win"
    return "You lose"

def play_game():
    """Play BlackJack."""
    print(logo)

    player_deck = []
    computer_deck = []
    is_game_over = False

    for _ in range(2):
        player_deck.append(deal_card())
        computer_deck.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_deck)
        computer_score = calculate_score(computer_deck)
        print(f"Your cards: {player_deck}, current score: {player_score}")
        print(f"Computer's first card: {computer_deck[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                player_deck.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_deck.append(deal_card())
        computer_score = calculate_score(computer_deck)

    print(f"Your final hand: {player_deck}, final score: {player_score}")
    print(f"Computer's final hand: {computer_deck}, final score: {computer_score}")
    print(compare(player_score, computer_score))

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    clear_console()
    play_game()


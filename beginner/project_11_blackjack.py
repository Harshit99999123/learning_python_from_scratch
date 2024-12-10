import random


def start_blackjack(cards):
    user_cards = []
    dealer_cards = []

    user_card1 = random.choice(cards)
    cards.remove(user_card1)
    user_card2 = random.choice(cards)
    cards.remove(user_card2)
    dealer_card1 = random.choice(cards)
    cards.remove(dealer_card1)
    dealer_cards.append(dealer_card1)
    dealer_card2 = random.choice(cards)
    cards.remove(dealer_card2)
    dealer_cards.append(dealer_card2)
    user_cards.append(user_card1)
    user_cards.append(user_card2)
    user_card_sum = cards_values.get(user_card1) + cards_values.get(user_card2)
    dealer_card_sum = cards_values.get(dealer_card1) + cards_values.get(dealer_card2)

    print(f"Computer first card is {dealer_card1}")

    if user_card_sum == blackjack_score:
        print(f"You have hit the blackjack with cards {user_cards}")
        return
    elif user_card_sum > blackjack_score:
        print(f"You have exceeded the blackjack score. Hence lost with the cards {user_cards} with score {user_card_sum}")
        return
    else:
        print(f"Your cards are {user_cards} with score {user_card_sum}")

    while user_card_sum < blackjack_score:
        hit_card = input("Do you want to hit: Y or N ")
        if hit_card.lower() == "y":
            next_user_card = random.choice(cards)
            cards.remove(next_user_card)
            user_card_sum += cards_values.get(next_user_card)
            print(f"New card chosen is {next_user_card}. Card sum is {user_card_sum}")
            user_cards.append(next_user_card)
            if user_card_sum == blackjack_score:
                print(f"You have hit the blackjack. Your cards: {user_cards}; Dealer cards: {dealer_cards}; Dealer "
                      f"score {dealer_card_sum}")
                return
            elif user_card_sum > blackjack_score:
                print(f"You have exceeded the blackjack score. You cards: {user_cards}; score {user_card_sum}; Dealer "
                      f"score {dealer_card_sum}")
                return
            else:
                print(f"Your cards: {user_cards}; score: {user_card_sum}. Dealer cards: {dealer_cards}; Dealer "
                      f"score: {dealer_card_sum}")
        else:
            break

    while dealer_card_sum < minimum_dealer_card_score:
        next_dealer_card = random.choice(cards)
        cards.remove(next_dealer_card)
        dealer_card_sum += cards_values.get(next_dealer_card)
        dealer_cards.append(next_dealer_card)

    if dealer_card_sum == blackjack_score:
        print(f"Dealer hit the jackpot. Dealer cards: {dealer_cards}; Your cards: {user_cards}; Your score: {user_card_sum}")
        return
    elif dealer_card_sum > blackjack_score:
        print(f"Dealer has exceeded the blackjack score. You cards: {user_cards}; score {user_card_sum}; Dealer cards: {dealer_cards}; Dealer"
              f" score {dealer_card_sum}")
        return
    if user_card_sum > dealer_card_sum:
        print(f"You win with the cards {user_cards}. Dealer cards are {dealer_cards}. Your score {user_card_sum} is "
              f"greater than dealer score {dealer_card_sum}")
    elif user_card_sum < dealer_card_sum:
        print(f"You lost with the cards {user_cards}. Dealer cards are {dealer_cards}. Your score {user_card_sum} is "
              f"less than dealer score {dealer_card_sum}")
    else:
        print(f"Match drawn. You cards are {user_cards}. Dealer cards are {dealer_cards}. Score is {user_card_sum}")


cards_values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "K": 10,
    "Q": 10,
    "J": 10
}
minimum_dealer_card_score = 17
blackjack_score = 21
play_blackjack = input("Do you wanna play blackjack? Y or n: ").lower().strip()

while play_blackjack == "y":
    cards = []
    for key in cards_values:
        for count in range(0, 4):
            cards.append(key)
    start_blackjack(cards)
    play_blackjack = input("Do you wanna play blackjack? Y or n: ").lower().strip()

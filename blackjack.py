import random
from ascii_art import blackjack_logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []


def play_blackjack():
    print(blackjack_logo)
    print("\nLet's play Blackjack! 🃏\n")

    def first_hand():
        print(f"\nYour cards: {your_cards} Score: {your_score}")
        print(f"Computer's card: {computer_cards[0]}")

    def final_hand():
        print(f"\nYour final hand: {your_cards} Score: {your_score}")
        print(f"Computer's final hand: {computer_cards} Score: {computer_score}")

    def winner(score1, score2, ending_scores):
        final_hand()
        if score1 == score2:
            print("Draw!")
        elif score1 == 21:
            print("You hit the road Jack!")
        elif score2 == 21:
            print("Computer hit the road Jack!")
        elif score1 > 21 and score1 == min(ending_scores):
            print("You win!")
        elif score2 > 21 and score2 == min(ending_scores):
            print("Computer wins!")
        elif not score1 > 21 and max(ending_scores) == score1:
            print("You win!")
        elif not score2 > 21 and max(ending_scores) == score2:
            print("Computer wins!")
        elif score1 > 21:
            print("Computer wins!")
        elif score2 > 21:
            print("You win!")

    def hit_winner(score1, score2):
        final_hand()
        if score1 > 21:
            print("Computer wins!")
        elif score2 > 21:
            print("You win!")
        elif score2 == 21:
            print("Computer hit the road Jack!")
        elif score1 == 21:
            print("You hit the road Jack!")
        elif score1 == score2:
            print("Draw!")

    def blackjack(score1, score2):
        if score1 == 21:
            final_hand()
            print("You hit the road Jack!")
        elif score2 == 21:
            final_hand()
            print("Computer hit the road Jack!")

    while True:
        your_cards = []
        computer_cards = []

        your_card1 = random.choice(cards)
        your_card2 = random.choice(cards)
        your_cards.extend([your_card1, your_card2])
        your_score = your_card1 + your_card2

        computer_card1 = random.choice(cards)
        computer_card2 = random.choice(cards)
        computer_cards.extend([computer_card1, computer_card2])
        computer_score = computer_card1 + computer_card2

        is_winner = False

        first_hand()
        blackjack(your_score, computer_score)
        if your_score >= 21 or computer_score >= 21:
            is_winner = True

        while not is_winner:
            is_winner = False
            hit_or_stand = input("\nHit or Stand? ").lower()

            while hit_or_stand == "hit":
                your_new_card = random.choice(cards)
                your_cards.append(your_new_card)
                your_score += your_new_card

                computer_new_card = random.choice(cards)
                computer_cards.append(computer_new_card)
                computer_score += computer_new_card

                if your_score > 21 and 11 in your_cards:
                    your_cards.remove(11)
                    your_cards.append(1)
                    your_score -= 10

                if computer_score > 21 and 11 in computer_cards:
                    computer_cards.remove(11)
                    computer_cards.append(1)
                    computer_score -= 10

                first_hand()
                if your_score >= 21 or computer_score >= 21:
                    is_winner = True
                    final_scores = [your_score, computer_score]
                    winner(your_score, computer_score, final_scores)
                    break
                hit_or_stand = input("\nHit or Stand? ").lower()

            else:
                if computer_score <= 16:
                    computer_new_card = random.choice(cards)
                    computer_cards.append(computer_new_card)
                    computer_score += computer_new_card

                final_scores = [your_score, computer_score]
                winner(your_score, computer_score, final_scores)
                is_winner = True
                break

        play_again = input("\nDo you want to play again? ")
        if play_again == "no":
            print("Thank you for playing. Goodbye!")
            break
        elif not play_again == "yes":
            print("Invalid input.")
            break

import random
from ascii_art import roulette_logo

pockets = [
    "00", "27", "10", "25", "29", "12", "8", "19", "31", "18",
    "6", "21", "33", "16", "4", "23", "35", "14", "2", "0",
    "28", "9", "26", "30", "11", "7", "20", "32", "17", "5",
    "22", "34", "15", "3", "24", "36", "13", "1"
]


def play_roulette():
    print(roulette_logo)

    def bet_on_pocket(balance, bet_amount, pocket_number):
        if bet_amount <= 0 or pocket_number < 0 or pocket_number > 36:
            print("Invalid bet amount or pocket number. Please try again.")
            return balance

        winning_pocket = random.choice(pockets)
        print("Winning pocket:", winning_pocket)

        if str(pocket_number) == winning_pocket:
            win_amount = bet_amount * 36
            print("Congratulations! You won $", win_amount)
            balance += win_amount
        else:
            print("Sorry, you lost $", bet_amount)
            balance -= bet_amount

        return balance

    def bet_on_color(balance, bet_amount, pocket_color):
        if bet_amount <= 0 or pocket_color not in ["red", "black"]:
            print("Invalid bet amount or pocket color. Please try again.")
            return balance

        winning_pocket = random.choice(pockets)
        print("Winning pocket:", winning_pocket)

        if (pocket_color == "red" and int(winning_pocket) % 2 == 1) or \
                (pocket_color == "black" and int(winning_pocket) % 2 == 0):
            win_amount = bet_amount * 2
            print("Congratulations! You won $", win_amount)
            balance += win_amount
        else:
            print("Sorry, you lost $", bet_amount)
            balance -= bet_amount

        return balance

    def bet_on_odd_even(balance, bet_amount, odd_even):
        if bet_amount <= 0 or odd_even not in ["odd", "even"]:
            print("Invalid bet amount or choice. Please try again.")
            return balance

        winning_pocket = random.choice(pockets)
        print("Winning pocket:", winning_pocket)

        if (odd_even == "odd" and int(winning_pocket) % 2 == 1) or \
                (odd_even == "even" and int(winning_pocket) % 2 == 0):
            win_amount = bet_amount * 2
            print("Congratulations! You won $", win_amount)
            balance += win_amount
        else:
            print("Sorry, you lost $", bet_amount)
            balance -= bet_amount

        return balance

    balance = 100

    while True:
        print("Balance: $", balance)

        print("\nSelect an option:")
        print("1. Bet on a pocket (number)")
        print("2. Bet on a pocket color (red or black)")
        print("3. Bet on odd or even")
        print("4. Quit the game")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            bet_amount = int(input("Enter the bet amount: "))
            pocket_number = int(input("Enter the pocket number: "))
            balance = bet_on_pocket(balance, bet_amount, pocket_number)
        elif choice == "2":
            bet_amount = int(input("Enter the bet amount: "))
            pocket_color = input("Enter the pocket color (red or black): ").lower()
            balance = bet_on_color(balance, bet_amount, pocket_color)
        elif choice == "3":
            bet_amount = int(input("Enter the bet amount: "))
            odd_even = input("Enter odd or even: ").lower()
            balance = bet_on_odd_even(balance, bet_amount, odd_even)
        elif choice == "4":
            print("\nThank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

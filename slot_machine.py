import random

symbols = ["🍒", "🍋", "🍉"]

while True:
    print("$Welcome to slots$\n")
    tokens = int(input("Enter Tokens: "))
    while tokens > 0:
        print(f"You have ", tokens, " tokens \n")
        try:
            action = input("Enter '1' to spin or '0' to cash out: ")
            if action == '0':
                print("Thanks for playing!\n")
                print("Your cash out is", tokens)
                break
            elif action == '1':
                bet = int(input("Bet amount: "))
            else:
                print("Invalid input! Please enter '1' to spin or '0' to cash out.")
                continue

        except ValueError:
            print("Please enter a whole number of tokens!")
            continue

        if bet > tokens:
            print("Not enough tokens.")
        else:
            tokens -= bet
            sq_one = random.choice(symbols)
            sq_two = random.choice(symbols)
            sq_three = random.choice(symbols)

            print()

            print("|", random.choice(symbols), "|", random.choice(symbols), "|", random.choice(symbols), "|")
            print("----------------")

            print("|", sq_one, "|", sq_two, "|", sq_three, "|")
            print("----------------")

            print("|", random.choice(symbols), "|", random.choice(symbols), "|", random.choice(symbols), "|")
            print("----------------")

            if sq_one == sq_two and sq_two == sq_three:
                amount_won = bet * 2
                print("You won", amount_won, "tokens!")
                tokens += amount_won
            else:
                print("You lost this time")

    if tokens == 0:
        print("\nYou are out of tokens.")
        print("Thanks for playing!")
        print("")
        print()
    break

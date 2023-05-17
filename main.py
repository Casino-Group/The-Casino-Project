import ascii_art
from blackjack import play_blackjack
from horse_betting import play_horse_betting

print(ascii_art.title)

menu = '''
What would you like to play?

1 -> Blackjack
2 -> Roulette
3 -> Slot Machine
4 -> Horse Betting
5 -> Exit

'''
casino = True
while casino:
    new_number = True
    while new_number:
        try:
            print("\n"+menu)
            game = int(input("Enter game option: "))
            new_number = False
        except ValueError as error:
            print("Please enter a number")

    match game:
        case 1:
            play_blackjack()
        case 2:
            print("You chose Roulette")
        case 3:
            print("You chose Slot Machine")
        case 4:
            play_horse_betting()
        case 5:
            casino = False
            print("Thank you for playing in the casino. Goodbye!")
        case _:
            print("You chose an invalid option")






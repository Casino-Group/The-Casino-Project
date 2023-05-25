import random
import tkinter as tk

# Define the symbols to use in the game
symbols = ["🍒", "🍋", "🍉"]


# Define the function to play the game
def play_game():
    global tokens
    # Get the bet amount from the user and validate the input
    try:
        bet = int(bet_entry.get())
    except ValueError:
        results_label.config(text="Please enter a valid bet amount.")
        return
    if bet <= 0:
        results_label.config(text="Please enter a positive bet amount.")
        return
    if bet > tokens:
        results_label.config(text="Not enough tokens.")
        return

    # Deduct the bet amount from the user's tokens
    tokens -= bet
    tokens_label.config(text="Tokens: {}".format(tokens))

    # Spin the slots
    rows = []
    for _ in range(3):
        row = [random.choice(symbols) for _ in range(3)]
        rows.append(row)

    # Display the results to the user
    slots_label.config(
        text="|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|".format(rows[0][0], rows[0][1], rows[0][2], rows[1][0], rows[1][1],
                                                         rows[1][2], rows[2][0], rows[2][1], rows[2][2]))

    # Calculate the winnings
    if rows[1][0] == rows[1][1] == rows[1][2]:
        amount_won = bet * 5
        tokens += amount_won
        results_label.config(text="You won {} tokens!".format(amount_won))
    else:
        results_label.config(text="You lost this time.")

    # Update the tokens label
    tokens_label.config(text="Tokens: {}".format(tokens))


# Define the function to check the token balance and exit the game
def checkout():
    global tokens
    results_label.config(text="You have {} tokens.".format(tokens))
    root.destroy()


# Create the main window
root = tk.Tk()
root.title("Slots Game")

# Create the widgets for the GUI
start_label = tk.Label(root, text="Enter the number of tokens to start with:")
start_entry = tk.Entry(root)
start_button = tk.Button(root, text="Start", command=lambda: start_game(int(start_entry.get())))
tokens_label = tk.Label(root, text="")
bet_label = tk.Label(root, text="Bet amount:")
bet_entry = tk.Entry(root)
play_button = tk.Button(root, text="Play", command=play_game)
slots_label = tk.Label(root, text="| | | |\n| | | |\n| | | |")
results_label = tk.Label(root, text="")
checkout_button = tk.Button(root, text="Checkout", command=checkout)

# Add the widgets to the window
start_label.pack()
start_entry.pack()
start_button.pack()
tokens_label.pack()
bet_label.pack()
bet_entry.pack()
play_button.pack()
slots_label.pack()
results_label.pack()
checkout_button.pack()


# Define the function to start the game
def start_game(start_tokens):
    global tokens
    tokens = start_tokens
    tokens_label.config(text="Tokens: {}".format(tokens))


# Start the game loop
root.mainloop()
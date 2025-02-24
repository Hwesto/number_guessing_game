'''
Number Guessing:
- User enters a casino-themed guessing game.
- Guess closest to 100; feedback on higher/lower.
- Lose 1/4 of the stake on wrong guesses, double on correct guesses.
'''

from random import randint  #Importing randint to generate random numbers between given ranges
import csv  #Used to handle high score persistence through CSV files
import time  #Used to add delays between prints for better user experience

def random_number():
    generated_number = randint(1,100)  #randint is inclusive of both ends (1 and 100)
    return(generated_number)  #Return passes value back to the caller (used in house_number assignment)

def higher_lower():
    print("""
    **********************************
    *                                *
    *    WELCOME TO HIGHER-LOWER!    *
    *  Guess the number to WIN BIG   *
    *                                *
    **********************************          
          """)  #Multi-line strings can be used for banners; triple quotes preserve formatting
    time.sleep(2)  #time.sleep adds delay (seconds); useful for pacing game flow
    
    print("\nIt's between 1 and 100, every time you guess wrong you lose a quarter of your stake, every time you win your bet doubles!")
    time.sleep(3)

    high_score = 100  #Initializes high_score; will be updated from the CSV file if exists
    high_score = high_score_display()  #Assigns the returned value (float) from the display function

    funds = 100  #Player's starting balance
    while True:  #Infinite loop for continuous play; breaks when user chooses "N"
        house_number = random_number()  #Random number generated each round
        time.sleep(1)
        print(f"\nCurrent Balance: ${funds}")  #f-strings are used for clean string formatting

        print("\nWould you like to play a round? ")
        play_status = input("\nY/N? ")  #Collecting user input (always returns a string)
        if play_status == "N":
            print("Thanks for playing!")  #Good practice to end with a friendly exit message
            break  #Break exits the while loop
        elif play_status == "Y":
            user_bet = user_bet_function(funds)  #Function returns a float bet amount; ensures input validation
            rounded_u_bet = round(user_bet, 2)  #round() limits to two decimals; avoids long float outputs
            funds -= rounded_u_bet  #Shorthand for funds = funds - rounded_u_bet

            winnings = guessing_game(rounded_u_bet, house_number, funds)  #Passes parameters into game loop
            funds += winnings  #Adds winnings back to player's funds
            high_score = high_score_function(high_score, funds)  #Updates and returns the new high score if beaten
        else:
            print("Y/N please.")  #Handles incorrect input

def high_score_function(high_score, funds):
    if funds > high_score:  #Comparison between float values; ensures correct data types
        high_score = funds  #Updates local variable
        with open("highscore.csv", "w", newline='') as document:  #"w" mode overwrites existing content
            writer = csv.writer(document)
            writer.writerow([high_score])  #Writes high_score as a single-item list
        print(f"New high score: ${high_score}")
    return high_score  #Always return high_score for next comparisons

def high_score_display():
    with open("highscore.csv", "r", newline='') as doc:  #"r" mode reads the existing file
        reader = csv.reader(doc)
        for row in reader:  #Iterates through CSV rows
            if row:  #Checks if the row isn’t empty
                high_score = float(row[0])  #Converts from string to float (important for numeric comparisons)
                return high_score  #Returns the high score for assignment in higher_lower()

    return 100  #Provides fallback if CSV is empty or not found

def guessing_game(rounded_u_bet, house_number, funds):
    count = 0  #Tracks number of guesses
    while True:
        time.sleep(1)
        print(f"\nNumber of Guesses Completed: {count}")
        try:
            user_guess_1 = int(input("Take a guess... "))  #int() conversion requires try-except for invalid inputs
            if 0 < user_guess_1 <= 100:  #Validates guess within range
                if user_guess_1 == house_number:  #Correct guess
                    winnings = rounded_u_bet * 2  #Doubles stake on correct guess
                    print(f"\nYou did it! You won ${winnings}")
                    return winnings  #Returns winnings to be added to funds
                else:
                    count += 1
                    print(advice(user_guess_1, house_number))  #Calls advice for directional feedback
                    rounded_u_bet = user_bet_rounding(rounded_u_bet)  #Updates stake after losing a quarter
                    time.sleep(2)
                    print(f"You lost a quarter! Current Stake: ${rounded_u_bet}")
            elif user_guess_1 == 0:  #Allows quitting mid-round
                print("You want to quit then... quitter.")
                return rounded_u_bet  #Returns remaining stake (refund)
            else:
                print("Are you jerking this casino around? Enter a number between 1 and 100.")
        except ValueError:  #Catches non-integer inputs (e.g., letters or symbols)
            print("You'll never win with that! Enter a valid number.")

def user_bet_rounding(rounded_u_bet):
    rounded = round(rounded_u_bet - (rounded_u_bet / 4), 2)  #Deducts 25% and rounds to two decimals
    return rounded  #Keeps calculations consistent (DRY principle)

def user_bet_function(funds):
    while True:
        try:
            print(" ")
            user_bet = float(input("How much do you want to bet? $"))  #Converts input to float; handles decimal bets
            if user_bet <= funds:  #Prevents betting more than available balance
                return user_bet  #Returns the validated bet
            else:
                print("You don't have that much!")  #Ensures bet is within funds limit
        except ValueError:  #Catches non-numeric inputs
            print("Enter a valid number...")

def advice(user_guess_1, house_number):
    if user_guess_1 < house_number:  #Guess is too low
        print()
        time.sleep(2)
        if (house_number - user_guess_1) < 40:
            return "You need to guess a little higher, you're less than 40 away!"
        else:
            return "You need to guess much higher, you're over 40 away!"
    else:  #Guess is too high
        if (user_guess_1 - house_number) < 40:
            return "You need to guess a little lower, you're less than 40 away!"
        else:
            return "You need to guess much lower, you're over 40 away!"

def main():
    higher_lower()  #Main game function call; handles full game flow

if __name__ == "__main__":  #Ensures code runs only when executed directly (not when imported)
    main()  #Calls main function to start the game

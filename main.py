'''
Number Guessing, User enters casino of gambling vs guess closest to 100, they get a higher or lower, if they're outside of 40 they get a ^^ extra higher or lower. if you lose, lose 1/4 money, gambled, if you win, gain double.

'''

from random import randint
import csv
import time

def random_number():
    generated_number = randint(1,100)
    return(generated_number)

def higher_lower():
    print("""
    **********************************
    *                                *
    *    WELCOME TO HIGHER-LOWER!    *
    *  Guess the number to WIN BIG   *
    *                                *
    **********************************          
          """)
    time.sleep(2)
    
    print ("\nIt's between 1 and 100, every time you guess wrong you lose a quarter of your stake, every time you win your bet doubles!")
    time.sleep(3)
    high_score = 100
    high_score=high_score_display()
    funds = 100
    while True:
        house_number = random_number()
        time.sleep(1)
        print (f"\nCurrent Balance: ${funds}")
        time.sleep(1)
        print("\nWould you like to play a round? ")
        play_status = input(("\nY/N? "))
        if play_status == "N":
            print ("Thanks for playing!")
            break
        elif play_status=="Y":
            user_bet = user_bet_function(funds)
            rounded_u_bet = round(user_bet,2)
            funds = funds - rounded_u_bet
            winnings = guessing_game(rounded_u_bet, house_number, funds)
            funds += winnings
            high_score = (high_score_function(high_score,funds))
        else: "Y/N please."

    
def high_score_function(high_score,funds):
    if funds > high_score:
        high_score = funds
        with open("highscore.csv", "w", newline='') as document:
            writer = csv.writer(document)
            writer.writerow([high_score])
        print (f"New high score: ${high_score}")
        return high_score
    return high_score
    
    
def high_score_display():
    with open("highscore.csv", "r", newline='') as doc:
        reader = csv.reader(doc)
        for row in reader:
            if row: 
                high_score = float(row[0])
                return high_score
            return high_score
    print (f"\nCurrent High Score: ${high_score}")
    
def guessing_game(rounded_u_bet, house_number, funds):
    count = 0
    while True:
        time.sleep(1)
        print (f"\nNumber of Guesses Completed: {count}")
        time.sleep(1)
        try:
            user_guess_1= int(input("Take a guess... "))
            if 0 < user_guess_1 <= 100:
                if user_guess_1 == house_number:
                    winnings = rounded_u_bet*2
                    print (f"\nYou did it! You won ${winnings}")
                    return winnings
                else:
                    count += 1
                    print(advice(user_guess_1,house_number))
                    rounded_u_bet = user_bet_rounding(rounded_u_bet)
                    time.sleep(2)
                    print (f"You lost a quarter! Current Stake: ${rounded_u_bet}")
            elif user_guess_1 == 0:
                print("You want to quit then.. quiter.")
                return rounded_u_bet
            else: 
                print("Are you jerking this casino around, give us a number between 1 and 100")
        except ValueError:
            print ("You'll never win with that Mwhaha")
            
            
def user_bet_rounding(rounded_u_bet):
    rounded = round((rounded_u_bet) - (rounded_u_bet/4),2)
    return rounded
    
    
def user_bet_function(funds):
    while True:
        try:
            print (" ")
            user_bet = float(input("How much do you want to bet? $"))
            if (user_bet<=funds):
                return user_bet
            else:
                print("You don't have that much")
        except ValueError:
            print("A number this time..")

def advice(user_guess_1, house_number):
    if (user_guess_1<house_number):
        print ()
        time.sleep(2)
        if ((house_number-user_guess_1)<40):
            return ("You need to guess a little higher, you're less than 40 away!")
        else:
            return ("You need to guess much higher, you're over 40 away!")
    else:
        if ((user_guess_1-house_number)<40):
            return ("You need to guess a little lower, you're less than 40 away!")
        else:
            return ("You need to guess much lower, you're over 40 away!")

def main():
    higher_lower()

if __name__ == "__main__":
    main()


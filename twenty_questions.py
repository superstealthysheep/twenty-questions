#generate random number
#prompt player for guess
#let user know how many guesses they have
#let player know if guess is too big or small, or if it is correct. 
#replayability


import random

default_guesses = 20
guess_list = []
guess_history = []
guesses_left = default_guesses
upper_limit = 2 ** default_guesses - 1

def show_help():
    print("""
    I'm thinking of an integer 1 to {}. You begin with {} guesses to find my number. 
    To show your guesses you have made and how many you have left, type SHOW
    To exit, type EXIT
    To show help again, type HELP""".format(upper_limit, default_guesses))
    
def show_guess_history():
    for guess in guess_history:
                print(str(guess))
    

def show_turns_remaining():
    print("You have {} turns remaining".format(default_guesses - len(guess_history)))

def game():
    
    guess_list = []
    guess_history = []
    guesses_left = default_guesses
    upper_limit = 2 ** default_guesses - 1
    
    #Generates random secret number
    secret_number = random.randint(1, upper_limit)
    
    show_help()
    new_guess = 0
    while len(guess_history) < default_guesses:
        #Prompts player for guess
        new_input = input(": ")
        
        #Shows help if player enters "HELP"
        if new_input == "HELP":
            show_help()
            continue
            
        #Shows guesses if player enters "SHOW"
        elif new_input == "SHOW":
            show_guess_history()
            show_turns_remaining()    
            continue
            
        elif new_input == "EXIT":
            exit()
                
        #Attempts to assign the input to an integer
        
        try:
            new_guess = int(new_input)
            
        #If the input can't be assigned to an integer, alert the player and allow them to retry.
        except ValueError:
            print("Oops! That wasn't a number. Try again.")
            continue
        
        #Checks the player's input against secret number
        if new_guess > secret_number:
            new_guess_results = ("({}) was too large. ".format(new_guess))
            guess_history.append(new_guess_results)
            turns_remaining = default_guesses - len(guess_history)
            print("Sorry, but your guess " + new_guess_results)
            
        elif new_guess < secret_number:
            new_guess_results = ("({}) was too small. ".format(new_guess))
            guess_history.append(new_guess_results)
            turns_remaining = default_guesses - len(guess_history)
            print("Sorry, but your guess " + new_guess_results)
            
        else:
            new_guess_results = ("({}) was the right answer!".format(new_guess))
            guess_history.append(new_guess_results)
            turns_remaining = default_guesses - len(guess_history)
            print("Nice! Your guess " + new_guess_results)
            print("You won with {} turns remaining!".format(turns_remaining))
            break
            
        
        
    if input("Play again? Y/n ") != "n":
        game()
        
game()
            

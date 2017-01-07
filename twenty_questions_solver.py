#show help
#ask how many questions they have
#allow user input
#tell user next guess

def show_help():
    print("""
    I am the companion program to twenty_questions.py
    I allow you to cheat. Just tell me how many guesses you were given when the prompt is >    
    After that, I'll tell you what number to guess next with prompt #. 
    You can report the results of your guess as <, =, or > when the prompt is :
    for if the mystery number is smaller, is correct, or is bigger, respectively.
    You can exit by telling me "EXIT".
    Show this help again by saying "HELP"
    """)
    
def close():
    print("Goodbye!")
    exit()

        
def game():
    
    #setup
    
    #shows the help
    show_help()
    
    #loops until broken
    while True:
        
        #asks user for number of guesses they started with
        new_input = input("How many guesses did you start with? ")
        
        #checks for commands
        if new_input == "EXIT":
            close()
            continue
            
        elif new_input == "HELP":
            show_help()
            continue
            
        #tries to make input an int
        try:
            default_guesses = int(new_input)
            
        #if it isn't an int, let them try again
        except ValueError:
            print("Oops! That isn't a number!")
            continue
            
        #if the number they give isn't greater than zero, let them try again
        if not default_guesses > 0:
            print("Whoops! You need to give me a number greater than 0.")
            continue
        
        #sets var guesses to equal the default number of guesses
        guesses = default_guesses
        
        #sets the upper and lower limits according to the guesses given
        upper_limit = 2 ** default_guesses - 1
        lower_limit = 1
        limit_average = (upper_limit + lower_limit)/2
        break
    

    
    
    #actual game
    while guesses > 0:
        #updates limit average
        limit_average = (upper_limit + lower_limit)/2
        
        #gives best guess and listens for response
        print("#{}".format(int(limit_average)))
        new_input = input(": ")
        
        #checks the response for commands and runs them
        if new_input == "EXIT":
            close()
            continue
              
        elif new_input == "HELP":
            show_help()
            continue
                
        
        #if the response is <, lower the upper limit
        if new_input == "<":
            upper_limit = limit_average - 1
            
        #if the response is =, deliver congratulations    
        elif new_input == "=":
            print("Congratualtions! Thanks to me you finished with {} tries left!".format(guesses))
            close()
            
        #if the response is >, raise the lower limit    
        elif new_input == ">":
            lower_limit = limit_average + 1
            
        #if the response isn't <=>, ask for another input    
        else:
            print("Hmmm... That wasn't a valid reply. If you need help, enter HELP.")
            continue
        
            
        
        guesses = guesses - 1
        
    #Once loop broken,
    print("It seems that you have run out of guesses. Next time you could maybe do a better job listening to me.")
    close()
    
game()
        

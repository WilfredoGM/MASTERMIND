# Egan Schmidt Weiss on Tue 30 Nov 15:40-15:55 Evaluated!
"""
Project III: An implementation of the Mastermind game

File Name: mastermind
Name:      ?
Course:    CPTR 141
Code Review:
"""
# Some variables are in Spanish
import random

# Random Color
random_code = []

# Colors
azul = "blue"
morado = "purple"
amarillo = "yellow"
naranga = "orange"
verde = "green"
rojo = "red"

# Flags
negro = "BLACK"
blanco = "WHITE"

# List of Valid Colors
colores = [azul, morado, amarillo, naranga, verde, rojo]

# lenght code
max_length = 4

# Guesses Variables
max_guesses = 10

# Errors
error_1 = "error1"
error_2 = "error2"

# Winnig Code
winner_feedback = [negro, negro, negro, negro]
win_check = "Ganador"

# Try again message
try_again = "Please check your answer and try again"

# Winner Message
win_message = "You won! Congrats!"

# Del
del1 = '-'
del2 = ''


def create_random_code():
    """ Post: creates a code using random module """
    for i in range(max_length):
        random_code.append(random.choice(colores))


def generate_feedback(guess_copy):
    """ 
    Pre: data is from user input
    Post: provides feedback to code 
    """
    feedback = []
    code = random_code.copy()
    guess = list(guess_copy)
    for i in range(max_length):
        if guess[i] == code[i]:
            code[i] = del1
            guess[i] = del2
            feedback.append(negro)
    for i in range(max_length):
        if guess[i] in code:
            match_position = find_match(guess[i])
            code[match_position] = del1
            guess[i] = del2
            feedback.append(blanco)
    winner = check_win(feedback)
    if winner == win_check:
        print(win_message)
        quit()
    else:
        return feedback


def find_match(guess_item):
    """ 
    Pre: data is from user input
    Post: finds the position of the matched colors 
    """
    code = random_code.copy()
    for i in range(max_length):
        if code[i] == guess_item:
            return i


def check_win(feedback):
    """ 
    Pre: data is from the feeback fuction
    Post: returns the winning code if player won 
    """
    if feedback == winner_feedback:
        return win_check
    else:
        print(f"Feedback: {feedback}")


def print_error_message(error_code):
    """ 
    Pre: data is from the validate_input function 
    Post: prints error messages based on user input 
    """
    if error_code == error_1:
        print(f"Please enter {max_length} colors.")
        print(try_again)
    elif error_code == error_2:
        print("Wrong color provided.")
        print(try_again)


def makeGuess(guess_count):
    """ 
    Pre: data is from the variable guess_count
    Post: returns a validated guess 
    """
    guess_left = max_guesses - guess_count
    print(f'\nNumber of guesses left: {guess_left}')
    guess = input("Enter your guess: ").split()
    validation_result = validate_input(guess)
    print_error_message(validation_result)
    while validation_result is not None:
        guess = input("Enter your guess: ").split()
        validation_result = validate_input(guess)
        print_error_message(validation_result)
    return guess


def validate_input(guess):
    """ 
    Pre: data is from user input
    Post: validates user input 
    """
    if len(guess) != max_length:
        return error_1
    for color in guess:
        if color not in colores:
            return error_2
    return None


def main():
    """ 
    Post: Main Game 
    """
    print()
    print("WELCOME TO MASTERMIND!")
    create_random_code()
    print(f"Each guess has to be {max_length} colors separated by a space.")
    print("The colors you may use:")
    print(f"{azul}, {morado}, {amarillo}, {naranga}, {verde} and {rojo}.")
    print(f"You get {max_guesses} guesses to decipher the code. Good luck!")
    guess_count = 0
    while guess_count <= max_guesses:
        if guess_count == max_guesses:
            print()
            print("You have exhausted your guesses. The Code was:")
            print(random_code)
            print()
            quit()
        else:
            guess = makeGuess(guess_count)
            generate_feedback(guess)
            guess_count += 1


main()

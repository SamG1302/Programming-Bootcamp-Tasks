from random import randint
# This code is a game where the user must correctly guess a randomly generated integer between 1 and 100.

# It first generates the answer (from 0 to 100) for the user to guess and welcomes the user to the game
# Then, we run a while loop. A while loop repeats a block of code as long as a specific condition is met.
# Let's run the while loop indefinitely by setting the condition to be True
# The main idea is to keep asking the user to guess until they get the right answer
# We do this through the following for each user's guess:
# - Validate the user's input i.e. check if it's an integer and if it's between 1 and 100 inclusive
#   - If the user's input is invalid i.e. not an integer between 1 and 100 inclusive, then reprompt the user to guess
#   - We do this by using 'continue', which essentially forces the code to run from the beginning of the while loop again, which then would ask the user to guess again
# - Check if the user's guess is less than the answer, equal to, or greater than the answer:
#   - If the user's input is equal to the answer, we congratulate the user for guessing the answer and exit out of the while loop using 'break' and end the game there
#   - If the user guess is less than the answer, tell the user that their guess is too low
#   - If the user guess is more than the answer, tell the user that their guess is too high
#  - By the nature of the while loop, if the user has guess incorrectly, it will simply ask the user to guess again, and repeat the whole process until they guess the answer right

def validate_input(user_guess: str) -> bool:
    """
    This section checks if the user input is valid. A valid user input is one where it is an integer and it is between 1 and 100 inclusive.

    :param user_guess: A string that is the user's input
    :return:    True if it is a valid input
                False if otherwise
    """

    if user_guess.isdigit(): # Checks if the user input (in the form of a string) is an integer
        if 1 <= int(user_guess) <= 100: # Now, we can safely convert it into an integer from a string, and then check if it's between 1 and 100 inclusive.
            return True

    else:
        print("This is not an integer that is between 1 and 100. Try again you fool!")
        return False

def guessed_correctly(user_guess: int, generated_answer: int) -> bool:
    """
    This checks whether the user's guess is either too low, too high, or equal to the answer and gives feedback to the user respectively.
    :param user_guess: An integer representing the user's guess
    :param generated_answer: An integer representing the answer to the game
    :return:    True if the user guessed correctly the answer
                False if the user guessed incorrectly
    """

    if user_guess < generated_answer:
        print("Your guess is too low, try a higher integer!")
        return False

    elif user_guess > generated_answer:
        print("Your guess is too high, try a lower integer!")
        return False

    else:
        return True

def main():
    """
    This is the main function of the game. On a very high-level, it:
        - Generates the answer for the user to guess
        - Keeps asking the user to guess the answer until they get the answer right.
        - For each guess:
            - Check if it's a valid input (i.e. an integer between 1 and 100 inclusive)
            - Check to see if their guess is correct.
                - If not, ask the user again to guess and repeat the entire process.
                - If the guess is correct, congratulate the user for winning and end the game.

    :return: None
    """

    generated_answer: int = randint(1, 100)
    print("Welcome to the guessing game! The goal is for you to guess an integer that I am thinking of between 1 and 100 inclusive")

    while True:
        user_guess: str = input("Guess your integer! Type your answer here: ")

        if not validate_input(user_guess):
            continue

        if guessed_correctly(int(user_guess), generated_answer):
            print("You have guessed the right integer!")
            break

if __name__ == '__main__':
    main()

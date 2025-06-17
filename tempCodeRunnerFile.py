
    This section checks if the user input is valid. A valid user input is one where it is an integer and it is between 1 and 100 inclusive.

    :param user_guess: A string that is the user's input
    :return:    True if it is a valid input
                False if otherwise
    """

    if user_guess.isdigit(): # Checks if the user input (in the form of a string) is an integer
        if 1 <= int(user_guess) <= 100: # Now, we can safely con
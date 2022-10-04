
def start():
    '''
    This function starts the guessing game loop logic. The function will poll and wait
    until the user inputs their guess and will exit once some conditions are met.
    '''

    answer = "sloth"
    guess_count = 0
    guess_limit = 3
    guess = None
    while guess_count < guess_limit:
        guess = input("Guess an animal: ").lower()
        guess_count += 1
        if guess == answer:
            print("Congratulations, you are correct! It is a sloth!")
            break
        if guess == "quit":
            break
        else:
            print("Sorry, you are incorrect. Try again!")
    return answer


start()

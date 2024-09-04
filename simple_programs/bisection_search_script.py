
def guessTheNumber():
    range_start = 0.0
    range_end = 100.0
    stop_program = False

    print('Please think of a number between 0 and 100!')

    while not stop_program:
        middle_point = int((range_end + range_start) / 2.0)

        print('Is your secret number ' + str(middle_point) + '?')

        answeer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

        if answeer == 'c':
            print("Game over. Your secret number was: " + str(middle_point))
            break
        elif answeer == 'l':
            range_start = middle_point
        elif answeer == 'h':
            range_end = middle_point
        else:
            print('Sorry, I did not understand your input.')
    

guessTheNumber()
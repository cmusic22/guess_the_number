import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'
total_guesses = 0


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)



def get_guess():
    '''get user's guess'''
    while True:
        try:
            return int(input('Guess the secret number? '))
        except ValueError:
            print('Bad input, Enter a number. ')
            continue
        break

def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    global total_guesses

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)
        total_guesses += 1

        if result == correct:

            print('You guessed the correct answer in ' + str(total_guesses) + ' tries.')
            break


if __name__ == '__main__':
    main()

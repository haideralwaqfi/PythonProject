from random import choice


def run_game():
    word: str = choice(['apple', 'orange', 'secret'])

    username: str = input('Enter your name: ')
    print(f'Welcome to gang man {username}')

    # Setup
    tries: int = 3
    guessed: str = ''

    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()  # Adds a blank line

        if blanks == 0:
            print('You Won!!!')
            break

        guess: str = input('Enter the letter: ')

        if guess in guessed:
            print(f'You already entered that letter: ({guess}), try another.')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Wrong! {tries} Tries Left.')

            if tries == 0:
                print('You lose the game :(')
                break


if __name__ == '__main__':
    run_game()

import random
import sys


def number_user_prompt(number_place: str):
    number: str = input(f'Please Enter the {number_place}: ')

    if number.lower() == 'exit':
        print('Thank You for playing')
        sys.exit()
    elif type(int(number)) == int:
        return number
    else:
        raise ValueError


def main():
    try:
        lower_number = number_user_prompt('Lower Number')
        higher_number = number_user_prompt('Higher Number')

        if lower_number > higher_number:
            print('Please make sure that the higher number is grater than than the lower number.')
            main()
        print(f'Your number between {lower_number} to {higher_number}')
        secret_number: int = random.randint(int(lower_number), int(higher_number))

        while True:
            user_guess: str = input('Your Guess: ')
            if user_guess.lower() == 'exit':
                print('Thank You for playing')
                sys.exit()

            if type(int(user_guess)) == int and int(user_guess) > secret_number:
                print('your guess greater than the number')
            elif type(int(user_guess)) == int and int(user_guess) < secret_number:
                print('your guess less than the number')
            elif type(int(user_guess)) == int and int(user_guess) == secret_number:
                print('your guess is Right!!!')
                print('start new game')
                main()
            else:
                print('Please enter a valid number!!!')
    except ValueError:
        print('Enter valid number')
        main()
    except Exception as e:
        print(f'Somthing went wrong : {e}')


if __name__ == '__main__':
    main()

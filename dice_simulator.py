import random

from typing import List


def roll_dice(amount: int = 2)-> List[int]:
    if amount <= 0:
        raise ValueError

    rolls: List[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1,6)
        rolls.append(random_roll)

    print(*rolls, sep=', ')

def main():
    try:
        while True:
            user_input: str = input('Enter amount of the rolling dice: ')

            if user_input.lower() == 'exit':
                print('Thank you for playing!!')
                break

            roll_dice(int(user_input))

    except ValueError:
        print('Please enter a valid number')

if __name__ == '__main__':
    main()

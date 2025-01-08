import itertools
import string
import sys
import time
from itertools import repeat

from typing import List


def common_guess(word: str) -> str or None:
    with open('words.txt', 'r') as words:
        word_list: List[str] = words.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common match: {match} (#{i})'


def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str or None:
    char: str = string.ascii_lowercase

    if digits:
        char += string.digits
    if symbols:
        char += string.punctuation

    attempts: int = 0
    for guess in itertools.product(char, repeat=length):
        attempts += 1
        guess: str = ''.join(guess)

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'


def main():
    while True:
        print('Searching...')
        user_input: str = input('Enter Your Word: ')
        if user_input.lower() == 'exit':
            sys.exit()
        start_time: float = time.perf_counter()

        if common_match:= common_guess(user_input):
            print(common_match)
        else:
            if cracked := brute_force(user_input, length=4, digits=True, symbols=True):
                print(cracked)
            else:
                print('There is no match...')

        end_time: float = time.perf_counter()
        print(round(end_time - start_time,2), 's')

if __name__ == '__main__':
    main()

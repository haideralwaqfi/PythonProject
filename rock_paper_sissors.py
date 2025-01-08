import random
import sys
from time import sleep

from typing import List


class RPS:
    def __init__(self):
        print('Welcome to RPS 9000!')

        self.moves: dict = {'rock': 'Rock', 'paper': 'Paper', 'scissors': 'Scissors'}
        self.valid_moves: List[str] = list(self.moves.keys())
        self.user_score: int = 0
        self.ai_score: int = 0

    def play_game(self):
        user_moves: str = input('Rock, Paper, Scissor? >> ').lower()

        if user_moves == 'exit':
            print('Thank you for playing...')
            sys.exit()

        if user_moves not in self.valid_moves:
            print('Please enter valid move...')
            self.play_game()
            return # Prevent further execution in the current function instance.

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_moves, ai_move)
        self.check_moves(user_moves, ai_move)
        self.display_score()

    def display_moves(self, user_move: str, ai_move: str):
        print('____')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('____')

    def display_score(self):
        print(f'Your score: {self.user_score}')
        print(f'AI score: {self.ai_score}')

    def check_moves(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print('Tie!')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You won!')
            self.user_score += 1
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You won!')
            self.user_score += 1
        elif user_move == 'paper' and ai_move == 'rock':
            print('You won!')
            self.user_score += 1
        else:
            print('AI won!')
            self.ai_score += 1




if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()

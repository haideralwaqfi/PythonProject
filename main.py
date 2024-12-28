# # # # # # # # from __future__ import annotations
# # # # # # # #
# # # # # # # # from random import choice
# # # # # # # # from datetime import datetime
# # # # # # # # from typing import Any
# # # # # # # #
# # # # # # # # from greetings import *
# # # # # # # # import string
# # # # # # # # from datetime import datetime
# # # # # # # # import time
# # # # # # # #
# # # # # # # # import requests
# # # # # # # # from requests import Response
# # # # # # # #
# # # # # # # # from my_package import website, internet
# # # # # # # #
# # # # # # # # import random
# # # # # # # # import sys
# # # # # # # #
# # # # # # # #
# # # # # # # # class Values:
# # # # # # # #     def __init__(self, value):
# # # # # # # #         self.value = value
# # # # # # # #
# # # # # # # #     def print_value_and_type(self):
# # # # # # # #         type_of_value = type(self.value)
# # # # # # # #         print(f'The value is: {self.value} and type of it is: {type_of_value}')
# # # # # # # #
# # # # # # # #
# # # # # # # # class Adder:
# # # # # # # #     def __init__(self):
# # # # # # # #         self.a = None
# # # # # # # #         self.b = None
# # # # # # # #         self.break_line: str = '==================='
# # # # # # # #
# # # # # # # #     def main(self):
# # # # # # # #         print(self.break_line)
# # # # # # # #         self.a: int = int(input('Enter value for a: '))
# # # # # # # #         self.b: int = int(input('Enter value for b:'))
# # # # # # # #         print(self.break_line)
# # # # # # # #         print(f'The Result is: {self.b + self.a}')
# # # # # # # #
# # # # # # # #
# # # # # # # # weather: dict = {
# # # # # # # #     'time': '12:00',
# # # # # # # #     'weather': {
# # # # # # # #         'morning': 'rain',
# # # # # # # #         'evening': 'more rain'
# # # # # # # #     }
# # # # # # # # }
# # # # # # # #
# # # # # # # #
# # # # # # # # class Story:
# # # # # # # #     def __init__(self):
# # # # # # # #         self.name: str = input('Enter a Name: ')
# # # # # # # #         self.noun: str = input('Enter a Noun: ')
# # # # # # # #         self.verb: str = input('Enter a Verb: ')
# # # # # # # #
# # # # # # # #     def main(self):
# # # # # # # #         story: str = f"""
# # # # # # # #         ------------------------------------------------------------------------------------
# # # # # # # #         This is a story of {self.name}, a strong (and beautiful) {self.noun} who
# # # # # # # #         loved to {self.verb}.
# # # # # # # #         ------------------------------------------------------------------------------------
# # # # # # # # """
# # # # # # # #         print(story)
# # # # # # # #
# # # # # # # #
# # # # # # # # class FullName:
# # # # # # # #     def __init__(self, f_name, m_name, l_name):
# # # # # # # #         self.f_name = f_name
# # # # # # # #         self.m_name = m_name
# # # # # # # #         self.l_name = l_name
# # # # # # # #         self.full_name: str = ''
# # # # # # # #         self.names: list = [self.f_name, self.m_name, self.l_name]
# # # # # # # #
# # # # # # # #     def main(self):
# # # # # # # #         for name in self.names:
# # # # # # # #             self.full_name += f'{name} '
# # # # # # # #         print(self.full_name)
# # # # # # # #
# # # # # # # #
# # # # # # # # class RockPaperScissors:
# # # # # # # #     def __init__(self):
# # # # # # # #         self.moves: dict = {'rock': 'Rock', 'paper': 'Paper', 'scissors': 'Scissors'}
# # # # # # # #         self.valid_moves: list = list(self.moves.keys())
# # # # # # # #         self.user_move = None
# # # # # # # #         self.ai_move = None
# # # # # # # #
# # # # # # # #     def prompts(self):
# # # # # # # #         while True:
# # # # # # # #             self.user_move: str = input('Rock, Paper, Scissors? >> ').lower()
# # # # # # # #             if self.user_move == 'exit':
# # # # # # # #                 print('Thank you for playing!')
# # # # # # # #                 sys.exit()
# # # # # # # #             if self.user_move not in self.valid_moves:
# # # # # # # #                 print('Invalid move...')
# # # # # # # #                 continue
# # # # # # # #             self.ai_move: str = random.choice(self.valid_moves)
# # # # # # # #             break
# # # # # # # #
# # # # # # # #     def choices(self):
# # # # # # # #         print('-------')
# # # # # # # #         print(f'You: {self.moves[self.user_move]}')
# # # # # # # #         print(f'Ai: {self.moves[self.ai_move]}')
# # # # # # # #         print('-------')
# # # # # # # #
# # # # # # # #     def check(self):
# # # # # # # #         if self.user_move == self.ai_move:
# # # # # # # #             print('It\'s a Tie')
# # # # # # # #         elif self.user_move == 'rock' and self.ai_move == 'scissors':
# # # # # # # #             print('You win!')
# # # # # # # #         elif self.user_move == 'scissors' and self.ai_move == 'paper':
# # # # # # # #             print('You win!')
# # # # # # # #         elif self.user_move == 'paper' and self.ai_move == 'rock':
# # # # # # # #             print('You win!')
# # # # # # # #         else:
# # # # # # # #             print('AI win...')
# # # # # # # #
# # # # # # # #     def run(self):
# # # # # # # #         print('Welcome to RPS')
# # # # # # # #         while True:
# # # # # # # #             self.prompts()
# # # # # # # #             self.choices()
# # # # # # # #             self.check()
# # # # # # # #
# # # # # # # #     def main(self):
# # # # # # # #         self.run()
# # # # # # # #
# # # # # # # #
# # # # # # # # def show_time():
# # # # # # # #     now: datetime = datetime.now()
# # # # # # # #     print(f'Time is: {now:%H:%M:%S}')
# # # # # # # #
# # # # # # # #
# # # # # # # # def greeting(name: str, language: str, default: str = 'Hello'):
# # # # # # # #     if language == 'it':
# # # # # # # #         print(f'Ciao, {name}')
# # # # # # # #     else:
# # # # # # # #         print(f'{default}, {name}')
# # # # # # # #
# # # # # # # #
# # # # # # # # def get_len_of_txt(txt: str) -> int:
# # # # # # # #     print(f'Getting the length of {txt} ...')
# # # # # # # #     return len(txt)
# # # # # # # #
# # # # # # # #
# # # # # # # # def txt_to_upper(txt: str) -> str:
# # # # # # # #     return txt.upper()
# # # # # # # #
# # # # # # # #
# # # # # # # # def add(*args: int) -> int:
# # # # # # # #     print(args)
# # # # # # # #     return sum(args)
# # # # # # # #
# # # # # # # #
# # # # # # # # def people_greeting(greet: str, *people: str, ending: str) -> None:
# # # # # # # #     for person in people:
# # # # # # # #         print(f'{greet}, {person} {ending}')
# # # # # # # #
# # # # # # # #
# # # # # # # # # def get_response(text: str) -> str:
# # # # # # # # #     lower: str = text.lower()
# # # # # # # # #
# # # # # # # # #     if lower == 'time':
# # # # # # # # #         return f'The time is {datetime.now()}'
# # # # # # # # #     elif lower in ['hello', 'hey', 'hi']:
# # # # # # # # #         return f'hey, there nice to meet you!'
# # # # # # # # #     elif lower == 'how are you?':
# # # # # # # # #         return f'fine, thank you!'
# # # # # # # # #     else:
# # # # # # # # #         return f'I don\'t understand the : "{text}"'
# # # # # # # # # while True:
# # # # # # # # #     user_res: str = input('you: ')
# # # # # # # # #     response: str = get_response(user_res)
# # # # # # # # #
# # # # # # # # #     if user_res == 'exit':
# # # # # # # # #         print('it was pleasure to see you :)')
# # # # # # # # #         sys.exit()
# # # # # # # # #     print(response)
# # # # # # # #
# # # # # # # #
# # # # # # # # def is_letters_only(text: str) -> None:
# # # # # # # #     alphabet: str = string.ascii_letters + ' '
# # # # # # # #
# # # # # # # #     for char in text:
# # # # # # # #         if char not in alphabet:
# # # # # # # #             raise ValueError('Text can only contains only from alphabet')
# # # # # # # #     print(f'"{text}" is only letters, good job!')
# # # # # # # #
# # # # # # # #
# # # # # # # # # def main() -> None:
# # # # # # # # #     while True:
# # # # # # # # #         user_input = input('your text is: ')
# # # # # # # # #         if user_input == 'exit':
# # # # # # # # #             sys.exit()
# # # # # # # # #         try:
# # # # # # # # #             is_letters_only(user_input)
# # # # # # # # #         except ValueError:
# # # # # # # # #             print('please enter valid text.')
# # # # # # # # #         except Exception as e:
# # # # # # # # #             print(f'We encounter an Error: {type(e)} | {e}')
# # # # # # # #
# # # # # # # #
# # # # # # # # def get_response(url: str) -> Response:
# # # # # # # #     return requests.get(url)
# # # # # # # #
# # # # # # # #
# # # # # # # # def show_response_info(response: Response) -> None:
# # # # # # # #     print('Status: ', response.status_code)
# # # # # # # #     print('OK: ', response.ok)
# # # # # # # #     print('Links: ', response.links)
# # # # # # # #     print('Encoding', response.encoding)
# # # # # # # #     print('Is permanent redirect: ', response.is_redirect)
# # # # # # # #
# # # # # # # #
# # # # # # # # # def main() -> None:
# # # # # # # # #     website: str = 'https://www.facebook.com/haideralwaqfi'
# # # # # # # # #     response: Response = get_response(website)
# # # # # # # # #     show_response_info(response)
# # # # # # # #
# # # # # # # #
# # # # # # # # # numbers: list[int] = [1,2,4,6]
# # # # # # # # # doubled_lc: list[int] = [number * 2 for number in numbers]
# # # # # # # #
# # # # # # # # # names: list[str] = ['James', 'Jamal', 'Haider', 'Ali', 'Ebaa']
# # # # # # # # # j_names: list[str] = [name for name in names if name.startswith('J')]
# # # # # # # # #
# # # # # # # # # numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # # # # # # # even_number_lc: list[int] = [number
# # # # # # # # #                              for number in numbers
# # # # # # # # #                              if number % 2 == 0]
# # # # # # # #
# # # # # # # # def welcome_message() -> None:
# # # # # # # #     print('Welcome to Groceries!')
# # # # # # # #     print('Enter:')
# # # # # # # #     print('-----------------')
# # # # # # # #     print('1 - To add an item')
# # # # # # # #     print('2 - To remove an item')
# # # # # # # #     print('3 - To list all item')
# # # # # # # #     print('0 - To the exit the program')
# # # # # # # #     print('-----------------')
# # # # # # # #
# # # # # # # #
# # # # # # # # def add_item(item: str, groceries: list[str]) -> None:
# # # # # # # #     groceries.append(item)
# # # # # # # #     print(f'"{item}" has been added!')
# # # # # # # #
# # # # # # # #
# # # # # # # # def remove_item(item: str, groceries: list[str]) -> None:
# # # # # # # #     try:
# # # # # # # #         groceries.remove(item)
# # # # # # # #         print(f'"{item}" has been removed!')
# # # # # # # #     except ValueError:
# # # # # # # #         print(f'NO "{item}" found in {groceries}')
# # # # # # # #
# # # # # # # #
# # # # # # # # def display(groceries: list[str]) -> None:
# # # # # # # #     print('___LIST___')
# # # # # # # #     for i, item in enumerate(groceries, 1):
# # # # # # # #         print(f'{i}: {item.capitalize()}')
# # # # # # # #     print('_' * 10)
# # # # # # # #
# # # # # # # #
# # # # # # # # def is_an_option(text: str) -> bool:
# # # # # # # #     return text in ['1', '2', '3', '0']
# # # # # # # #
# # # # # # # #
# # # # # # # # #
# # # # # # # # # def main() -> None:
# # # # # # # # #     groceries: list[str] = []
# # # # # # # #
# # # # # # # # # welcome_message()
# # # # # # # # # while True:
# # # # # # # # #     user_input: str = input('Chose: ')
# # # # # # # # #
# # # # # # # # #     if not is_an_option(user_input):
# # # # # # # # #         print('Please Enter Valid Option...')
# # # # # # # # #         continue
# # # # # # # # #
# # # # # # # # #     if user_input == '1':
# # # # # # # # #         new_item: str = input('What item would you like to add:? >> ').lower()
# # # # # # # # #         add_item(new_item, groceries)
# # # # # # # # #     elif user_input == '2':
# # # # # # # # #         item_to_remove: str = input('What item would you like to remove? >> ').lower()
# # # # # # # # #         remove_item(item_to_remove, groceries)
# # # # # # # # #     elif user_input == '3':
# # # # # # # # #         display(groceries)
# # # # # # # # #     elif user_input == '0':
# # # # # # # # #         print('Exiting The Program')
# # # # # # # # #
# # # # # # # #
# # # # # # # # # class Car:
# # # # # # # # #     SPEED_LIMIT_PER_KM: int = 140
# # # # # # # # #
# # # # # # # # #     def __init__(self, brand: str, ) -> None:
# # # # # # # # #         self.brand = brand
# # # # # # # # #
# # # # # # # # #     def drive(self, *, speed: float) -> None:
# # # # # # # # #         if speed > self.SPEED_LIMIT_PER_KM:
# # # # # # # # #             print(f'Limiter activated: Driving as {self.SPEED_LIMIT_PER_KM}kw/h')
# # # # # # # # #         else:
# # # # # # # # #             print(f'Driving at {speed}km/h')
# # # # # # # #
# # # # # # # #
# # # # # # # # # class Book:
# # # # # # # # #     def __init__(self, title: str, pages: int) -> None:
# # # # # # # # #         self.title = title
# # # # # # # # #         self.pages = pages
# # # # # # # # #
# # # # # # # # #     def __len__(self) -> int:
# # # # # # # # #         return self.pages
# # # # # # # # #
# # # # # # # # #     def __add__(self, other: Self) -> Self:
# # # # # # # # #         combined_title: str = f'{self.title} & {other.title}'
# # # # # # # # #         combined_title: int = self.pages + other.pages
# # # # # # # #
# # # # # # # #
# # # # # # # # # def main() -> None:
# # # # # # # # #     pydaily: Book = Book('pydaily', 100)
# # # # # # # # #     harry_potter: Book = Book('Harry Potter', 340)
# # # # # # # # #     print(len(pydaily))
# # # # # # # # #     print(len(harry_potter))
# # # # # # # # #
# # # # # # # # #     combined_books : Book = pydaily + harry_potter
# # # # # # # # #     print(combined_books.title, combined_books.pages)
# # # # # # # #
# # # # # # # # class ChatBot:
# # # # # # # #     def __init__(self, name: str, age: int) -> None:
# # # # # # # #         self.name = name
# # # # # # # #         self.age = age
# # # # # # # #
# # # # # # # #     def get_description(self) -> str:
# # # # # # # #         return f'{self.name} is a bot who is {self.age} years old.'
# # # # # # # #
# # # # # # # #     def get_response(self, text: str) -> str:
# # # # # # # #         lowered: str = text.lower()
# # # # # # # #
# # # # # # # #         if 'hello' in lowered:
# # # # # # # #             return f'{self.name}: Hey there!'
# # # # # # # #         elif 'bye' in lowered:
# # # # # # # #             return f'{self.name}: See you!'
# # # # # # # #         elif 'how old are you' in lowered:
# # # # # # # #             return f'{self.name}: I am {self.age} years old'
# # # # # # # #         elif 'what time is it' in lowered:
# # # # # # # #             now: datetime = datetime.now()
# # # # # # # #             return f'{self.name}: The current time is {now:%H:%M:%S}'
# # # # # # # #         elif 'how are you' in lowered:
# # # # # # # #             return f'{self.name}: Great, thanks!'
# # # # # # # #         else:
# # # # # # # #             random_choices: list[str] = ['I don\'t understand...', 'What?', 'Ah, what?']
# # # # # # # #             return f'{self.name}: {choice(random_choices)}'
# # # # # # # #
# # # # # # # #     def run(self) -> None:
# # # # # # # #         while True:
# # # # # # # #             user_input: str = input('You: ')
# # # # # # # #             if user_input == 'exit':
# # # # # # # #                 print(f'Thank you for chatting with {self.name}!')
# # # # # # # #                 break
# # # # # # # #             response: str = self.get_response(user_input)
# # # # # # # #             print(response)
# # # # # # # #
# # # # # # # #
# # # # # # # # # def main()->None:
# # # # # # # # #     people : list[str] = ['haider','ebaa','ali']
# # # # # # # # # i :int = 1
# # # # # # # # # for person in people:
# # # # # # # # #     print(f'{i}: {person}.')
# # # # # # # # #     i+=1
# # # # # # # # # for i, person in enumerate(people, start=1):
# # # # # # # # #     print(i, person, sep=": ", end='. \n')
# # # # # # # # # my_range: range = range(0,-5, -1)
# # # # # # # # # print(my_range)
# # # # # # # # # print(list(my_range))
# # # # # # # # # txt : str = 'hello world'
# # # # # # # # # first_three: slice = slice(0,3)
# # # # # # # # # reversed_txt: slice = slice(None, None, -1)
# # # # # # # # # print(txt[reversed_txt])
# # # # # # # #
# # # # # # # # # my_locals: dict[str,Any] = dict(locals())
# # # # # # # # # print(my_locals)
# # # # # # # #
# # # # # # # # # requirements: dict[str, bool] = {
# # # # # # # # #     'connected to net': True,
# # # # # # # # #     'wifi': True,
# # # # # # # # #     'secure': False
# # # # # # # # # }
# # # # # # # # # print(requirements)
# # # # # # # # # start_check: list[bool] = []
# # # # # # # # # for k, v in requirements.items():
# # # # # # # # #     print(v)
# # # # # # # # #     start_check.append(v)
# # # # # # # # #
# # # # # # # # # if all(start_check):
# # # # # # # # #     print('Okay!!!')
# # # # # # # # # else:
# # # # # # # # #     print('not all requirements satisfied')
# # # # # # # #
# # # # # # # # # from difflib import get_close_matches
# # # # # # # # #
# # # # # # # # # def get_best_match(user_question: str, knowledge: dict) -> str | None:
# # # # # # # # #     questions: list[str] = [q for q in knowledge]
# # # # # # # # #     matches: list[str] = get_close_matches(user_question, questions, n=1, cutoff=0.6)
# # # # # # # # #
# # # # # # # # #     if matches:
# # # # # # # # #         return matches[0]
# # # # # # # # #
# # # # # # # # # def run_chatbot(knowledge: dict) -> None:
# # # # # # # # #     while True:
# # # # # # # # #         user_input: str = input('You: ')
# # # # # # # # #
# # # # # # # # #         best_match: str | None = get_best_match(user_input, knowledge)
# # # # # # # # #         response: str | None = knowledge.get(best_match)
# # # # # # # # #
# # # # # # # # #         if response:
# # # # # # # # #             print(f'Bot: {response}')
# # # # # # # # #         else:
# # # # # # # # #             print(f'Bot: I do not understand...')
# # # # # # # # #
# # # # # # # # # def main() -> None:
# # # # # # # # #     brain: dict[str, str] = {
# # # # # # # # #         'hello': 'Hi There!',
# # # # # # # # #         'How are you': 'I am good!!',
# # # # # # # # #         'ok': 'great'
# # # # # # # # #     }
# # # # # # # # #     run_chatbot(knowledge=brain)
# # # # # # # #
# # # # # # # # #
# # # # # # # # # def main() -> None:
# # # # # # # # # numbers: list[int] = list(range(1, 21))
# # # # # # # # # print(numbers)
# # # # # # # #
# # # # # # # # # def is_even(number: int) -> bool:
# # # # # # # # #     return number % 2 == 0
# # # # # # # #
# # # # # # # # # even: filter[int] = filter(lambda n: n % 2 == 0, numbers)
# # # # # # # # # print(list(even))
# # # # # # # # # print(numbers)
# # # # # # # # #
# # # # # # # # # people: list[str] = ['haider', 'ali', 'ebaa', ]
# # # # # # # # # ln: list[str] = [name for name in people if len(name) > 3]
# # # # # # # # # print(ln)
# # # # # # # # # long_name: filter[str] = filter(lambda p: len(p) > 3, people)
# # # # # # # # # print(list(long_name))
# # # # # # # #
# # # # # # # # # def main() -> None:
# # # # # # # # #     # numbers : list[int] = list(range(1,21))
# # # # # # # # #     # double_number: list[int] = [n * 2 for n in numbers]
# # # # # # # # #     # print(double_number)
# # # # # # # # #
# # # # # # # # #     # numbers: list[int] = [1,2,3]
# # # # # # # # #     # names: list[str] = ['haider', 'ali', 'ebaa']
# # # # # # # # #     #
# # # # # # # # #     # def combined(number: int, name: str)->tuple[int, str]:
# # # # # # # # #     #     return number, name
# # # # # # # # #     #
# # # # # # # # #     # combined_tuple: map = map(lambda number, name: {number, name}, numbers, names)
# # # # # # # # #     # print(list(combined_tuple))
# # # # # # # # #
# # # # # # # # #     people_list: list[str] = ['haider', 'ebaa', 'ali']
# # # # # # # # #
# # # # # # # # #     sorted_people: list[str] = sorted(people_list, key=lambda x: len(x), reverse=True)
# # # # # # # # #     print(sorted_people)
# # # # # # # #
# # # # # # # # from dataclasses import dataclass, field, InitVar
# # # # # # # # from uuid import uuid4, UUID
# # # # # # # #
# # # # # # # #
# # # # # # # # @dataclass
# # # # # # # # class Note:
# # # # # # # #     id: UUID = field(init=False)
# # # # # # # #     title: str
# # # # # # # #     body: str
# # # # # # # #
# # # # # # # #     def __post_init__(self) -> None:
# # # # # # # #         self.id = uuid4()
# # # # # # # #
# # # # # # # #
# # # # # # # # class NoteApp:
# # # # # # # #     def __init__(self, author: str, notes: list[Note] | None = None) -> None:
# # # # # # # #         self.author = author
# # # # # # # #
# # # # # # # #         if notes is None:
# # # # # # # #             self._notes = []
# # # # # # # #         else:
# # # # # # # #             self._notes = notes
# # # # # # # #
# # # # # # # #         self.display_instructions()
# # # # # # # #
# # # # # # # #     @staticmethod
# # # # # # # #     def display_instructions() -> None:
# # # # # # # #         print('Welcome to notes!')
# # # # # # # #         print('Here is the commends:')
# # # # # # # #         print('1- add ')
# # # # # # # #         print('2- edit')
# # # # # # # #         print('3- delete')
# # # # # # # #         print('4- display all')
# # # # # # # #
# # # # # # # #     def _add_note(self) -> None:
# # # # # # # #         title: str = input('Title: ')
# # # # # # # #         body: str = input('Body: ')
# # # # # # # #
# # # # # # # #         note: Note = Note(title, body)
# # # # # # # #         self._notes.append(note)
# # # # # # # #         print('Note was added!')
# # # # # # # #
# # # # # # # #     def _edit_note(self) -> None:
# # # # # # # #         print('Which note would you like to edit?')
# # # # # # # #         self._show_notes()
# # # # # # # #
# # # # # # # #         try:
# # # # # # # #             note_index: int = int(input('Note index')) - 1
# # # # # # # #             current: Note = self._notes[note_index]
# # # # # # # #
# # # # # # # #             new_title: str = input('New title: ')
# # # # # # # #             new_body: str = input('New Body: ')
# # # # # # # #
# # # # # # # #             current.title = new_title
# # # # # # # #             current.body = new_body
# # # # # # # #             print('Note was updated!')
# # # # # # # #         except IndexError:
# # # # # # # #             print('Please select a valid note index...')
# # # # # # # #             self._edit_note()
# # # # # # # #         except ValueError:
# # # # # # # #             print('Index cannot be empty')
# # # # # # # #             print('operation aborted')
# # # # # # # #
# # # # # # # #     def _delete_note(self) -> None:
# # # # # # # #         print('Which note would you like to delete?')
# # # # # # # #         self._show_notes()
# # # # # # # #
# # # # # # # #         try:
# # # # # # # #             note_index: int = int(input('Index: ')) - 1
# # # # # # # #             del self._notes[note_index]
# # # # # # # #             print('Note was deleted!')
# # # # # # # #         except IndexError:
# # # # # # # #             print('Please select a valid note index...')
# # # # # # # #             self._delete_note()
# # # # # # # #         except ValueError:
# # # # # # # #             print('Index cannot be empty')
# # # # # # # #             print('operation aborted')
# # # # # # # #
# # # # # # # #     def _show_notes(self) -> None:
# # # # # # # #         if not self._notes:
# # # # # # # #             print('No Notes...')
# # # # # # # #             return
# # # # # # # #         for i, note in enumerate(self._notes, start=1):
# # # # # # # #             print(f'[{i}] {note.title}: {note.body}')
# # # # # # # #
# # # # # # # #     def _select_option(self, user_input:str)-> None:
# # # # # # # #         if user_input not in ['1', '2', '3', '4']:
# # # # # # # #             print('Please pick a valid one')
# # # # # # # #             return
# # # # # # # #         if user_input == '1':
# # # # # # # #             self._add_note()
# # # # # # # #         elif user_input == '2':
# # # # # # # #             self._edit_note()
# # # # # # # #         elif user_input == '3':
# # # # # # # #             self._delete_note()
# # # # # # # #         elif user_input == '4':
# # # # # # # #             self._show_notes()
# # # # # # # #
# # # # # # # #     def run_app(self)-> None:
# # # # # # # #         while True:
# # # # # # # #             user_input: str = input('You: ')
# # # # # # # #             self._select_option(user_input)
# # # # # # # #
# # # # # # # # def main() -> None:
# # # # # # # #     sample_notes: list[Note] = [Note(title='Title1', body='Hello there, Bob!'),
# # # # # # # #                                 Note(title='Title2', body='More text!')]
# # # # # # # #     note_app: NoteApp = NoteApp(author='bob', notes=sample_notes)
# # # # # # # #     note_app.run_app()
# # # # # # # #
# # # # # # # # if __name__ == "__main__":
# # # # # # # #     main()
# # # # # # #
# # # # # # # import asyncio
# # # # # # # import contextvars
# # # # # # # import functools
# # # # # # # from asyncio import Task, Future
# # # # # # # from datetime import  datetime
# # # # # # #
# # # # # # # from typing import Any, Dict
# # # # # # #
# # # # # # # import requests
# # # # # # # from requests import  Response
# # # # # # #
# # # # # # # async def to_thread(func, /, *args, **kwargs):
# # # # # # #     loop = asyncio.get_running_loop()
# # # # # # #     ctx = contextvars.copy_context()
# # # # # # #     func_call = functools.partial(ctx.run, func, *args, **kwargs)
# # # # # # #     return await loop.run_in_executor(None, func_call)
# # # # # # #
# # # # # # # async def check_status(url: str) -> Dict[str, Any]:
# # # # # # #     start_time: datetime = datetime.now()
# # # # # # #     response: Response = await to_thread(requests.get, url, None)
# # # # # # #     end_time: Response = datetime.now()
# # # # # # #
# # # # # # #     return {
# # # # # # #         'website': f'{url}',
# # # # # # #         'status': response.status_code,
# # # # # # #         'start_time': f'{start_time:%H:%M:%S}',
# # # # # # #         'end_time': f'{end_time:%H:%M:%S}',
# # # # # # #
# # # # # # #     }
# # # # # # #
# # # # # # # async def main() -> None:
# # # # # # #     print('fetching the results')
# # # # # # #     tasks: Future = asyncio.gather(
# # # # # # #         check_status('https://bing.com'),
# # # # # # #         return_exceptions=True
# # # # # # #     )
# # # # # # #
# # # # # # #     results: list[dict] = await tasks
# # # # # # #     print(results)
# # # # # # #
# # # # # # #     for result in results:
# # # # # # #         print(result)
# # # # # # #
# # # # # # #
# # # # # # # if __name__ == '__main__':
# # # # # # #     asyncio.run(main=main())
# # # # # # from collections.abc import Callable
# # # # # # from nis import match
# # # # # # from typing import Dict, List
# # # # # #
# # # # # #
# # # # # # def main() -> None:
# # # # # #     # def for_each(values: List[int], f: Callable) -> None:
# # # # # #     #     for value in values:
# # # # # #     #         f(value)
# # # # # #     #
# # # # # #     # for_each([2, 4, 6, 8, 10], lambda v: print(v * 'X'))
# # # # # #
# # # # # #     # names: List[str]= ['Bob', 'Car', 'Airplane']
# # # # # #     # sorted_names: List[str] = sorted(names, key= lambda name: name.lower())
# # # # # #     # print(sorted_names)
# # # # # #
# # # # # #     # from typing import Generator
# # # # # #     # def huge_data() -> Generator:
# # # # # #     #     for i in range(1, 100_000_000):
# # # # # #     #         yield i
# # # # # #     #
# # # # # #     # data: Generator = huge_data()
# # # # # #     # for n in range(200):
# # # # # #     #     print(next(data))
# # # # # #
# # # # # #
# # # # # #
# # # # # # if __name__ == '__main__':
# # # # # #     main()
# # # # # from collections.abc import Callable
# # # # # from functools import wraps
# # # # # from time import sleep
# # # # # from typing import Any, List
# # # # #
# # # # # # def repeat(number: int) -> Callable:
# # # # # #     """Repeat function amount of times"""
# # # # # #
# # # # # #     def decorator(func: Callable) -> Callable:
# # # # # #         @wraps(func)
# # # # # #         def wrapper(*args, **kwargs) -> Any:
# # # # # #             value: Any = None
# # # # # #             for _ in range(number):
# # # # # #                 value = func(*args, **kwargs)
# # # # # #
# # # # # #             return value
# # # # # #
# # # # # #         return wrapper
# # # # # #
# # # # # #     return decorator
# # # # # #
# # # # # # @repeat(3)
# # # # # # def greeting(name):
# # # # # #     print(f'hello {name}')
# # # # #
# # # # # import time
# # # # # from functools import cached_property
# # # # # import logging
# # # # #
# # # # # # class DataSet:
# # # # # #     def __init__(self, data: List[float]) -> None:
# # # # # #         self._data = data
# # # # # #
# # # # # #     def show_data(self) -> None:
# # # # # #         print(self._data)
# # # # # #
# # # # # #     @cached_property
# # # # # #     def sum(self) -> float:
# # # # # #         print('Calculating Sum...')
# # # # # #         time.sleep(2)
# # # # # #         return sum(self._data)
# # # # # #
# # # # # #     @cached_property
# # # # # #     def mean(self) -> float:
# # # # # #         print('Calculating Mean...')
# # # # # #         time.sleep(2)
# # # # # #         return sum(self._data) / len(self._data)
# # # # # #
# # # # # #
# # # # # # def main() -> None:
# # # # # #     ds: DataSet = DataSet([1.5, 2, 3, 4.5, 6.8])
# # # # # #     ds.show_data()
# # # # # #
# # # # # #     while True:
# # # # # #         user_input: str = input('You: ').lower()
# # # # # #
# # # # # #         if user_input == 'clear sum':
# # # # # #             del ds.sum
# # # # # #             print('Sum cache delete!!')
# # # # # #         elif user_input == 'clear mean':
# # # # # #             del ds.mean
# # # # # #             print('Mean cache deleted!!')
# # # # # #         elif user_input == 'sum':
# # # # # #             print(ds.sum)
# # # # # #         elif user_input == 'mean':
# # # # # #             print(ds.mean)
# # # # # #         else:
# # # # # #             print('Unknown Commend')
# # # # # #
# # # # # class
# # # # #
# # # # # if __name__ == '__main__':
# # # # #     main()
# # # #
# # # # import time
# # # # import logging
# # # #
# # # # class Internet:
# # # #     def __init__(self, provider: str)->None:
# # # #         self.provider = provider
# # # #
# # # #     def connect(self)->None:
# # # #         print(f'[{self.provider}] Connecting...')
# # # #         time.sleep(2)
# # # #         print(f'[{self.provider}] You are connected')
# # # #
# # # # def main()->None:
# # # #     internet: Internet = Internet('Zain')
# # # #     internet.connect()
# # # #
# # # # if __name__ == '__main__':
# # # #     main()
# # #
# # # import logging
# # #
# # #
# # # def new_print(text) -> None:
# # #     logging.warning(text)
# # #
# # # print = new_print
# # #
# # # def main()->None:
# # #     print('Hi')
# # #
# # # if __name__ == '__main__':
# # #     main()
# #
# # from timeit import timeit, repeat
# #
# # a : str = 'list(range(1000))'
# # b: str = 'set(range(1000))'
# #
# # a_time : float = timeit(stmt=a, number=100_000)
# # b_time : float = timeit(stmt=b, number=100_000)
# #
# # print(f'a: {a_time:.3f}s')
# # print(f'b: {b_time:.3f}s')
# import json
# from typing import TextIO
#
# file_path: str = 'info.txt'
# # file: TextIO = open(file_path)
# # text: str = file.read()
# # print(text)
# # file.close()
#
# data: dict = {'name' : 'haider', 'last_name': 'alwaqfi', 'age': 33, 'job': None}
#
#
# try:
#     with open('new_json_file', 'w') as file:
#         json.dump(data, file)
# except FileNotFoundError:
#     print('file not exist')


import sys


class Notepad:
    def __init__(self, author: str, file_name: str) -> None:
        self.author = author
        self._file_name = file_name

    def _show_instructions(self) -> None:
        print(f'Welcome to Notepad, {self.author}!')
        print('Commands:')
        print('1 - write note')
        print('2 - display note')
        print('0 - exit Notepad')

    def _write_note(self) -> None:
        user_input: str = input('Enter a Note: ')

        with open(self._file_name, 'w') as note:
            note.write(user_input)

    def _display_note(self) -> None:
        try:
            with open(self._file_name, 'r') as note:
                text: str = note.read()
                print(f'Bot: {text}')
        except FileNotFoundError:
            print('Bot: file does not exist')

    def _exit_notepad(self) -> None:
        print(f'See You next time, {self.author}')
        sys.exit()

    def run(self) -> None:
        self._show_instructions()
        while True:
            user_input: str = input(f'{self.author}: ')

            if user_input not in ('0', '1', '2'):
                print('Bot: Please enter a valid choice.')
                continue
            if user_input == '1':
                self._write_note()
            elif user_input == '2':
                self._display_note()
            elif user_input == '0':
                self._exit_notepad()
            else:
                print('Bot: unknown commend!')


def main() -> None:
    def add(a: int = 4, b: int = 0) -> int:
        return a + b

    print(add(5))


if __name__ == '__main__':
    main()

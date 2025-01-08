import sys
from typing import List


def common_passoword(password: str):
    with open('password.txt', 'r') as file:
        common_passwords: List[str] = file.read().splitlines()

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{password}: X (#{i})')
            return
    print(f'{password}: (Unique)')



def main():
    while True:

        user_password: str = input('Enter your password: ')
        if user_password == '':
            print('Please Enter a valid password!')
            continue
        elif user_password.lower() == 'exit':
            sys.exit()

        common_passoword(user_password)

if __name__ == '__main__':
    main()
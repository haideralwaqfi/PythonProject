import secrets
import string

from typing import List


def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    if length < 1:
        raise ValueError('The length of password must be not less than 2 character')

    combination: str = string.ascii_lowercase + string.digits
    password: List[str] = []

    if symbols:
        combination += string.punctuation
        password.append(secrets.choice(string.punctuation))
    if uppercase:
        combination += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(secrets.choice(combination))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


if __name__ == '__main__':
    for i in range(1, 6):
        new_pass: str = generate_password(2, symbols=True, uppercase=True)
        specs: str = f'{i} --> {new_pass} (U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)})'
        print(specs)

from typing import Final

AUTHOR: Final[str]= 'Haider'
VERSION: Final[float] = 0.1

def greet(name:str) -> None:
    print(f'hello {name}!')


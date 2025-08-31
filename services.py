# services.py
from typing import List

listOfNumber: List[int] = []
max_value: int = 0

def start_counter(counter: int) -> List[int]:
    global listOfNumber
    listOfNumber = [0 for _ in range(counter)]
    return listOfNumber

def return_value(index: int) -> int:
    return listOfNumber[index]

def increment(index: int) -> int:
    global max_value
    listOfNumber[index] += 1
    max_value = listOfNumber[index]
    return listOfNumber[index]

def set_max() -> List[int]:
    global listOfNumber, max_value
    listOfNumber = [max_value for _ in listOfNumber]
    return listOfNumber

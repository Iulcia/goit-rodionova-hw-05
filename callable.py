""""This fnc seraches all real numbers from text and returns total of founded numbers"""

import re
from typing import Callable
from functools import reduce


def generator_numbers(text: str):
    words = text.split(" ")
    real_number = r'\d+[\.,]{0,1}\d+.' # regex for serching numbers in string
    numbers = map(float,filter(lambda x: re.match(real_number,x), words)) # get all numbers by regexp from list of words
    for number in numbers:
        yield number

def sum_profit(text: str, func: Callable):
    return reduce(lambda x,y:x+y, func(text))


#text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
#total_income = sum_profit(text, generator_numbers)
#print(f"Загальний дохід: {total_income}")

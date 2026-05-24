import re
from typing import Callable


def generator_numbers(input_text: str):
    numbers = re.findall(r"\d+(?:\.\d+)?", input_text)

    for number in numbers:
        yield float(number)


def sum_profit(input_text: str, func: Callable) -> float:
    return sum(func(input_text))


text = (
    "Загальний дохід працівника складається "
    "з декількох частин: 1000.01 як основний дохід, "
    "доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")



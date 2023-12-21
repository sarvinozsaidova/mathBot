import random
from enum import Enum


class Operations(Enum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"


class DifficultyEnum(Enum):
    LIGHT = 1
    MEDIUM = 2
    HARD = 3


def choose_operation():
    operation = random.choice(list(Operations))
    return operation.value


def generate_number(minimal, maximal):
    return random.randint(minimal, maximal)


def get_result(first_num, second_num, operation):
    return int(eval(f"{first_num}{operation}{second_num}"))


def get_nums_borders(user_choice, operation):
    first_num_borders = []
    second_num_borders = []
    if operation == Operations.ADDITION.value or operation == Operations.SUBTRACTION.value:
        if user_choice == DifficultyEnum.LIGHT.name:
            first_num_borders = [1, 99]
            second_num_borders = first_num_borders
        elif user_choice == DifficultyEnum.MEDIUM.name:
            first_num_borders = [10, 1000]
            second_num_borders = first_num_borders
        elif user_choice == DifficultyEnum.HARD.name:
            first_num_borders = [100, 10000]
            second_num_borders = first_num_borders

    elif operation == Operations.MULTIPLICATION.value:
        if user_choice == DifficultyEnum.LIGHT.name:
            first_num_borders = [1, 9]
            second_num_borders = first_num_borders
        elif user_choice == DifficultyEnum.MEDIUM.name:
            first_num_borders = [1, 99]
            second_num_borders = [1, 9]
        elif user_choice == DifficultyEnum.HARD.name:
            first_num_borders = [1, 99]
            second_num_borders = [1, 99]

    elif operation == Operations.DIVISION.value:
        if user_choice == DifficultyEnum.LIGHT.name:
            first_num_borders = [1, 99]
            second_num_borders = [1, 10]
        elif user_choice == DifficultyEnum.MEDIUM.name:
            first_num_borders = [1, 99]
            second_num_borders = [1, 99]
        elif user_choice == DifficultyEnum.HARD.name:
            first_num_borders = [99, 9999]
            second_num_borders = [10, 999]
    return first_num_borders, second_num_borders


def make_divisible(first_num, second_num):
    if first_num < second_num:
        first_num, second_num = second_num, first_num

    reminder = first_num % second_num
    if reminder:
        first_num -= reminder
    return first_num, second_num


def get_task(user_difficulty_choice):
    operation = choose_operation()
    first_num_borders, second_num_borders = get_nums_borders(user_difficulty_choice, operation)
    first_num = generate_number(first_num_borders[0], first_num_borders[1])
    second_num = generate_number(second_num_borders[0], second_num_borders[1])

    if operation == Operations.DIVISION.value:
        first_num, second_num = make_divisible(first_num, second_num)
    result = get_result(first_num, second_num, operation)
    task = f"{first_num} {operation} {second_num}"
    return {
        "task": task,
        "result": result,
    }






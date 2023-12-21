from aiogram.dispatcher.filters.state import StatesGroup, State


class MathState(StatesGroup):
    difficulty = State()
    task = State()
    correct_answer = State()
    user_answer = State()

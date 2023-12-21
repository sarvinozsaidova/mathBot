from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from math_tasks import DifficultyEnum


start_game_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_btn = KeyboardButton(text="/start_quiz")
start_game_kb.add(start_btn)


difficulty_kb = InlineKeyboardMarkup()
light_btn = InlineKeyboardButton(
    text=DifficultyEnum.LIGHT.name,
    callback_data=DifficultyEnum.LIGHT.name
)
medium_btn = InlineKeyboardButton(
    text=DifficultyEnum.MEDIUM.name,
    callback_data=DifficultyEnum.MEDIUM.name
)
hard_btn = InlineKeyboardButton(
    text=DifficultyEnum.HARD.name,
    callback_data=DifficultyEnum.HARD.name
)
difficulty_kb.add(light_btn)
difficulty_kb.add(medium_btn)
difficulty_kb.add(hard_btn)


def get_during_game_kb(show_answer=False):
    during_game_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    stop_btn = KeyboardButton(text="/stop_quiz")
    during_game_kb.add(stop_btn)
    if show_answer:
        show_answer_btn = KeyboardButton(text="/javob_ko`rsatish")
        during_game_kb.insert(show_answer_btn)
    return during_game_kb


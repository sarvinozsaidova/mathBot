from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from confik import TOKEN
from keyboards import start_game_kb
from fsm import MathState
from keyboards import difficulty_kb
from keyboards import get_during_game_kb
from math_tasks import get_task


bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def get_new_task(state: FSMContext):
    data = await state.get_data()
    task_data = get_task(data["difficulty"])
    await state.update_data(correct_answer=task_data["result"])
    await state.update_data(task=task_data["task"])
    return task_data["task"]


@dp.message_handler(commands="start")
async def start(message: Message):
    await message.answer("Salom  !!!", reply_markup=start_game_kb)


@dp.message_handler(commands="start_quiz")
async def start_quiz(message: Message, state: FSMContext):
    await state.set_state(MathState.difficulty)
    during_game_kb = get_during_game_kb()
    await message.answer(
        "O'yinni to'xtatish uchun /stop_quiz buyrug'ini yuboring",
        reply_markup=during_game_kb
    )
    await message.answer(
        "Qiyinchilikni tanlang",
        reply_markup=difficulty_kb
        )


@dp.message_handler(state="*", commands="stop_quiz")
async def stop_quiz(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("To`xtatildi", reply_markup=start_game_kb)


@dp.callback_query_handler(state=MathState.difficulty)
async def set_difficulty(cb: CallbackQuery, state: FSMContext):
    await state.update_data(difficulty=cb.data)
    await state.set_state(MathState.user_answer)
    task = await get_new_task(state)
    during_game_kb = get_during_game_kb(show_answer=True)
    await cb.message.answer(task, reply_markup=during_game_kb)


@dp.message_handler(state=MathState.user_answer, commands="show_answer")
async def show_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"To`gri javob: {data['correct_answer']}")
    task = await get_new_task(state)
    await message.answer(task)


@dp.message_handler(state=MathState.user_answer)
async def check_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    user_answer = message.text.strip()
    if user_answer == str(data["correct_answer"]):
        task = await get_new_task(state)
        return await message.answer(task)
    return await message.answer(data["task"])


if __name__ == "__main__":
    executor.start_polling(dp)






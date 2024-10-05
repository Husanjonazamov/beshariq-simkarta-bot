# aiogram import
from aiogram.types import Message

# kode import
from loader import dp
from utils import texts, buttons



@dp.message(lambda message: message.text == '/start')
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text=texts.START_MESSAGE,
        reply_markup=buttons.MENU_BUTTON
    )
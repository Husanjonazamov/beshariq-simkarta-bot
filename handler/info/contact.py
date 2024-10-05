# aiogram import
from aiogram.types import Message

# kode import
from loader import dp
from utils import texts, buttons



@dp.message(lambda message: message.text == buttons.MENU_BUTTON.keyboard[1][0].text)
async def contact(message: Message) -> None:
    await message.answer(
        text=texts.CONTACT_MESSAGE,
    )
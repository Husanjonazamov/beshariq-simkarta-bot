# aiogram import
from aiogram.types import Message

# kode import
from loader import dp
from utils import buttons



@dp.message(lambda message: message.text == buttons.MENU_BUTTON.keyboard[1][1].text)
async def location(message: Message) -> None:
    latitude = 40.436599
    longitude = 70.605132
    
    await message.answer_location(latitude=latitude, longitude=longitude)
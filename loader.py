# aiogram import
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from env import BOT_TOKEN as TOKEN
    
dp = Dispatcher()

# Initialize Bot instance with default bot properties which will be passed to all API calls
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)
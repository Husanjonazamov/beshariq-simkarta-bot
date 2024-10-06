from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,\
                          ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, WebAppInfo


REMOVE_BUTTON = ReplyKeyboardRemove()


BACK_BUTTON = KeyboardButton(text="⬅️ Orqaga qaytish")

BACK = ReplyKeyboardMarkup(
    keyboard=[
        [
            BACK_BUTTON
        ],
    ], resize_keyboard=True
)

MENU_BUTTON = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Raqam tanlash", web_app=WebAppInfo(url='https://beshsim.seezntv.uz/')),
        ],
    ], resize_keyboard=True
)

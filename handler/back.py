# aiogram import
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

# kode import
from loader import dp
from utils import texts, buttons


# get back to main menu
@dp.message(lambda message: message.text == buttons.BACK_BUTTON.text)
async def back_to_menu(message: Message, state:FSMContext) -> None:

    await message.answer(
        text=texts.BACK_MAIN_MENU,
        reply_markup=buttons.MENU_BUTTON
    )

    # end state
    await state.clear()

# get back to main company
@dp.message(lambda message: message.text == buttons.BACK_BUTTON.text)
async def back_to_menu(message: Message, state:FSMContext) -> None:
    await message.answer(
        text=texts.BACK_COMPANYS,
        reply_markup=buttons.COMPANYS
    )
    


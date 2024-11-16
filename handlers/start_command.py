from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.main_menu import MainMenu  # Новий імпорт
import logging

router = Router()
logger = logging.getLogger(__name__)

@router.message(CommandStart())
async def start_command(message: types.Message):
    user_name = message.from_user.first_name

    welcome_text = f'''
🎮 *Вітаю, {user_name}!* 🎮

🌟 Я твій особистий помічник у світі Mobile Legends: Bang Bang! 🌟

Використовуйте кнопки внизу для навігації:
• 🦸‍♂️ Герої - інформація про героїв
• 🎯 Мета - актуальний мета-звіт
• 🛠️ Білди - гайди по білдам
• ❓ Допомога - додаткова інформація

_Готовий допомогти тобі стати кращим гравцем!_ 💪
'''

    try:
        menu = MainMenu()
        keyboard = await menu.get_keyboard()
        
        await message.answer(
            text=welcome_text, 
            parse_mode="Markdown",
            reply_markup=keyboard
        )
        logger.info(f"Відправлено привітання користувачу {user_name} (ID: {message.from_user.id})")
    except Exception as e:
        logger.error(f"Помилка при відправці привітання: {e}")
        await message.answer("Вітаю! Я бот Mobile Legends. Використовуйте кнопки знизу для навігації.")
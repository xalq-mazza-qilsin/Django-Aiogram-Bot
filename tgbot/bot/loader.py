from src.settings import API_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode


bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

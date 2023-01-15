from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import config

storage = MemoryStorage()
bot = Bot(token=config['bot']['token'])
dp = Dispatcher(bot,storage=storage)


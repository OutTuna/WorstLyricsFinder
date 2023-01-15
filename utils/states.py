from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    artist = State()
    song = State()   
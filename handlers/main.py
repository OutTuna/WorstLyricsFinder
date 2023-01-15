import hashlib
from aiogram import types
from aiogram.dispatcher import FSMContext
from load import dp, bot
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle

from utils.states import Form
from utils.worker import lyrics_getter



@dp.message_handler(commands =['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi, there u can take all textes from genius.com\nCreated by @OutTuna & @fuksys")
    await finder(message)


@dp.message_handler(state=None)
async def finder(message: types.Message):
    await bot.send_message(message.chat.id, "Nazvanie pidorsa plz syka: ")
    await Form.artist.set()


@dp.message_handler(state = Form.artist)
async def artists_name(message:types.Message, state: FSMContext):
    await state.update_data(artist=message.text)
    await bot.send_message(message.chat.id,f"Name Artist is:{message.text}")
    await bot.send_message(message.chat.id, "Song")
    await Form.song.set()

@dp.message_handler(state=Form.song)
async def song_name(message:types.Message, state: FSMContext):
    await state.update_data(song=message.text)
    current_state = await state.get_data()
    await state.finish()
    song_text = lyrics_getter(**current_state)
    await bot.send_message(message.chat.id, song_text)
    await finder(message)

@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    data = inline_query.query.split("-") # Exapmle: @yourBot Artist - Song name
    try:
        text = lyrics_getter(*data)
        input_content = InputTextMessageContent(text)
        result_id: str = hashlib.md5(text.encode()).hexdigest()
        item = InlineQueryResultArticle(
            id=result_id,
            title=f'Result {text!r}',
            input_message_content=input_content,
        )
        await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)
    except Exception: pass

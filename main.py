from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import re
from dotenv import load_dotenv
import os

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

@dp.message(Command(commands=['caps']))
async def process_caps_command(message: Message):
    if message.text is not None:
        await message.answer(text=message.text.split('/caps')[1].upper())
    else:
        await message.answer("Текст не обнаружен")

@dp.message(Command(commands=['reverse']))
async def process_caps_command(message: Message):
    if message.text is not None:
        await message.answer(text=message.text.split('/reverse')[1][::-1])
    else:
        await message.answer("Текст не обнаружен")

@dp.message(
    lambda msg: any(
        word in re.sub(r'[^\w\s]', '', msg.text.lower())  # Удаляет все знаки препинания
        for word in ['привет', 'здравствуйте', 'ку', 'хай', 'хелло',
                     'доброе утро', 'добрый день', 'добрый вечер', 'здарова']
    )
)
async def send_hello(message: Message):
    await message.answer(text=f'Привет, {message.from_user.first_name}')

@dp.message(F.photo)
async def send_photo(message: Message):
    if message.caption is not None:
        await message.reply(text=f' Что это за {message.caption}')
    else:
        await message.reply("Данный формат пока не поддерживается")

@dp.message()
async def send_echo(message: Message):
    if message.text is not None:
        await message.reply(text=message.text)
    else:
        await message.reply("Текст не обнаружен")

if __name__ == '__main__':
    dp.run_polling(bot)
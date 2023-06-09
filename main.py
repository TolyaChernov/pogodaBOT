import math

import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from key import key, token_api

bot = Bot(token=key)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды")


@dp.message_handler()
async def get_weather(message: types.Message):
    q = message.text
    try:
        response = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={token_api}&q={q}&lang=ru&aqi=no"
        )
        data = response.json()
        print(data)
        city = data["location"]["name"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        pressure_mb = data["current"]["pressure_mb"]
        wind_mph = data["current"]["wind_mph"]
        condition = data["current"]["condition"]["text"]

        await message.reply(
            f"\nГород: {city}\nСтрана: {country}\nМестное время: {localtime}\nТемпература: {temp}°C\nПогодные условия: {condition}\n"
            f"Влажность: {humidity}%\nДавление: {math.ceil(pressure_mb/1.333)} мм.рт.ст\nВетер: {wind_mph} м/с \n"
            f"Хорошего дня!"
        )

    except Exception as exc:
        await message.reply(f"Проверьте название города!")


if __name__ == "__main__":
    executor.start_polling(dp)

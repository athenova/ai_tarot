import os
import telebot
import schedule
import time
from openai import OpenAI
from datetime import datetime

AI_TEXT_MODEL = 'chatgpt-4o-latest'
BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
#CHAT_ID = -1002374309134
CHAT_ID = '@ai_tarot'

def job(sign, CHAT_ID=CHAT_ID):
    today = datetime.today().strftime('%Y-%m-%d')
    client = OpenAI()
    text = client.chat.completions.create(
        model=AI_TEXT_MODEL,
        messages=[
            { "role": "system", "content": f"Ты - профессиональный таролог" },
            { "role": "user", "content": f"Составь таро-гороскоп на {today} для знака '{sign}', используй смайлики, не пиши дату" },
        ]
    ).choices[0].message.content
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")

if __name__ == '__main__':
    schedule.every().day.at("09:00",'Europe/Moscow').do(job, sign="Рыбы")
    schedule.every().day.at("09:01",'Europe/Moscow').do(job, sign="Овен")
    schedule.every().day.at("09:02",'Europe/Moscow').do(job, sign="Телец")
    schedule.every().day.at("09:03",'Europe/Moscow').do(job, sign="Близнецы")
    schedule.every().day.at("09:04",'Europe/Moscow').do(job, sign="Рак")
    schedule.every().day.at("09:05",'Europe/Moscow').do(job, sign="Лев")
    schedule.every().day.at("09:06",'Europe/Moscow').do(job, sign="Дева")
    schedule.every().day.at("09:07",'Europe/Moscow').do(job, sign="Весы")
    schedule.every().day.at("09:08",'Europe/Moscow').do(job, sign="Скорпион")
    schedule.every().day.at("09:09",'Europe/Moscow').do(job, sign="Стрелец")
    schedule.every().day.at("09:10",'Europe/Moscow').do(job, sign="Козерог")
    schedule.every().day.at("09:11",'Europe/Moscow').do(job, sign="Водолей")

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)

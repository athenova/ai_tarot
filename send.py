from project import Project
import schedule
import time


def job(type, **kwargs):
    p = Project()
    p.send(type, **kwargs)

if __name__ == '__main__':
    p = Project()

    schedule.every().day.at("09:00",'Europe/Moscow').do(job, type="pisces", chat_id='@pisces_the')
    schedule.every().day.at("09:01",'Europe/Moscow').do(job, type="aries", chat_id='@aries_the')
    schedule.every().day.at("09:02",'Europe/Moscow').do(job, type="taurus")
    schedule.every().day.at("09:03",'Europe/Moscow').do(job, type="gemini", chat_id='@gemini_the')
    schedule.every().day.at("09:04",'Europe/Moscow').do(job, type="cancer")
    schedule.every().day.at("09:05",'Europe/Moscow').do(job, type="leo")
    schedule.every().day.at("09:06",'Europe/Moscow').do(job, type="virgo")
    schedule.every().day.at("09:07",'Europe/Moscow').do(job, type="libra")
    schedule.every().day.at("09:08",'Europe/Moscow').do(job, type="scorpio")
    schedule.every().day.at("09:09",'Europe/Moscow').do(job, type="sagittarius")
    schedule.every().day.at("09:10",'Europe/Moscow').do(job, type="capricorn", chat_id='@capricorn_the')
    schedule.every().day.at("09:11",'Europe/Moscow').do(job, type="aquarius", chat_id='@aquarius_the')

    fifteen_minutes = 15 * 60

    for i in range(fifteen_minutes):
        schedule.run_pending()
        time.sleep(1)

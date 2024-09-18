# notifier.py

from telegram import Bot
import smtplib
from email.mime.text import MIMEText
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_TO

# Функция для отправки сообщения в Telegram


def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

# Функция для отправки Email


def send_email(subject, content):
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = EMAIL_TO

    server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(EMAIL_HOST_USER, EMAIL_TO, msg.as_string())
    server.quit()

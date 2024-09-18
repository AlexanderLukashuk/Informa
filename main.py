# main.py

from news_fetcher import get_news
from summarizer import summarize_article
from notifier import send_telegram_message, send_email


def main():
    query = "technology"
    news = get_news(query)

    for article in news:
        title = article['title']
        url = article['url']
        # Контент для выжимки
        content = article['content'] or article['description']

        if content:
            summary = summarize_article(content)
            message = f"Title: {title}\nURL: {url}\n\nSummary:\n{summary}"

            # Отправка уведомлений
            send_telegram_message(message)
            # send_email(subject=f"News Summary: {title}", content=message)


if __name__ == "__main__":
    main()

# news_fetcher.py

from newsapi import NewsApiClient
from config import NEWSAPI_KEY

newsapi = NewsApiClient(api_key=NEWSAPI_KEY)


def get_news(query):
    articles = newsapi.get_everything(q=query,
                                      sources='the-verge',  # Указываем источник
                                      language='en',
                                      sort_by='publishedAt')
    return articles['articles'] if 'articles' in articles else []

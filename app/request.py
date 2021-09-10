from app.models.news_test import News
from app import app
import urllib.request,json
from .models import news


News=news.News
#Getting api key
api_key = app.config['NEWS_API_KEY']

#getting the news  base url
base_url=app.config['NEWS_API_URL_ALL']
base_url_article=app.config['NEWS_ARTICLE_ALL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=6e5882a38e5f40e9bad1a2742e5d9c9e'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources = process_results(news_sources_list)


    return news_sources

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_sources = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category=news_item.get('category')
        country=news_item.get('country')
        if description:
            news_object = News(id,name,description,url,category,country)
            news_sources.append(news_object)

    return news_sources    
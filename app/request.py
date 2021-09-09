from app.models.news_test import News
from app import app
import urllib.request,json
from .models import news


News=news.News
#Getting api key
api_key = app.config['NEWS_API_KEY']

#getting the news  base url
base_url=app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        url_image = news_item.get('url_image')
        publisherAt=news_item.get('publisherAt')
        content=news_item.get('content')
        if description:
            news_object = news(id,author,title,description,url,url_image,publisherAt,content)
            news_results.append(news_object)

    return news_results    
from app import app
import urllib.request,json
from .models import news


News=news.News
AllArticles=news.AllArticles
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

        news_sources = None

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
        language=news_item.get('language')
        country=news_item.get('country')
        if description:
            news_object = News(id,name,description,url,category,country,language)
            news_sources.append(news_object)

    return news_sources    

def get_news_allarticles(sources):
    '''
    function to retrieve data from database of newsapi
    '''  

    get_news_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=6e5882a38e5f40e9bad1a2742e5d9c9e'.format(sources)

    with urllib.request.urlopen(get_news_articles_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources_articles = None

        if get_news_response['articles']:
            news_sources_list = get_news_response['articles']
            news_sources_articles = process_results(news_sources_list)


    return news_sources_articles

def process_articles(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_sources_articles = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage=news_item.get('urlToImage')
        content=news_item.get('content')
        if description:
            news_object = AllArticles(author,title,description,url,urlToImage,content)
            news_sources_articles.append(news_object)

    return news_sources_articles   

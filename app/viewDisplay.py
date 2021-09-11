
# from app.models.news import AllArticles
from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_news_allarticles,search_news
#ViewDisplay
@app.route('/')
def index():
    '''
    ViewDisplay root page function that retruns the index page and its data
    '''
    bussiness_news=get_news()
    print(bussiness_news)
    title="Welcome to Newspaper Application Streaming"
    # =====search goes here====
    search_movie = request.args.get('news_query')
    if search_movie:
        return redirect(url_for('search',news_name=search_movie))
    else:
        return render_template('index.html', title = title, bussiness=bussiness_news )

    # =======
    # return render_template('index.html',title=title,bussiness=bussiness_news)

@app.route('/bussiness/<id>')  
def bussiness(id):
    '''
     ViewDisplay root page function that retruns the bussiness page and its data
    '''  
    Allarticles_news=get_news_allarticles(id)
    print(Allarticles_news)
    # title="Kuo: Apple Watch Series 7 is a ‘dramatic change in design’, will be released this month despite initial production issues - 9to5Mac"
    return render_template('bussiness.html', Allarticles=Allarticles_news)

# ============search goes here==============
@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)


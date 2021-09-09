
from flask import render_template
from app import app
from .request import get_news
#ViewDisplay
@app.route('/')
def index():
    '''
    ViewDisplay root page function that retruns the index page and its data
    '''
    bussiness_news=get_news('bussiness')
    print(bussiness_news)
    title="Welcome to Newspaper Application Streaming"
    return render_template('index.html',title=title,bussiness=bussiness_news)

@app.route('/bussiness')  
def bussiness():
    '''
     ViewDisplay root page function that retruns the bussiness page and its data
    '''  
    title="Current and Tredings  Todays Bussiness News "
    return render_template('bussiness.html',title=title)

@app.route('/technology')
def technology():
    '''
     ViewDisplay root page function that retruns the technology page and its data
    '''  
    title="Current and Tredings  Technology News Updates " 
    return render_template('technology.html', title=title) 
@app.route('/sports')
def sports():
    '''
     ViewDisplay root page function that retruns the sports page and its data
    '''   
    title="Current and Tredings  Sports News Updates "
    return render_template('sports.html', title=title)
@app.route('/entertain')
def entertain():
    '''
     ViewDisplay root page function that retruns the entertainment page and its data
    '''  
    title="Current and Tredings Entertainments News Updates"   
    return render_template('entertain.html', title=title)


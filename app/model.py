class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count



# from os import name
from urllib.request import urlopen


class News:
    '''
#     News class to define News Objects
#     '''

#     def __init__(self,id,name,description,url,category,country,language): 
#     # def __init__(self,author,title,description,url,urlToImage,content):
#         self.id =id
#         self.name = name
#         self.description =description
#         self.url=url
#         self.language=language
#         self.category = category
#         self.country=country
        

# class Allarticles:
#     '''
#     method to get all the articles
#     '''        
#     def __init__(self,author,title,description,url,urlToImage,publisherAt,content):
#         '''
#         method to display the objects
#         '''
#         self.author=author
#         self.title=title
#         self.description=description
#         self.url=url
#         self.urlToImage=urlToImage
#         self.publisherAt=publisherAt
#         self.content=content
    
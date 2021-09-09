class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,author,title,description,url,url_image,publisherAt,content):
        self.id =id
        self.author = author
        self.title = title
        self.description =description
        self.url=' "https://www.macrumors.com/2021/09/08/dutch-bank-de-volksbank-apple-pay-support/'+ url
        self.url_image ='https://images.macrumors.com/t/tzJhmO9DcRnY3jtlKgvHUk2kZfQ=/2500x/https://images.macrumors.com/article-new/2021/04/apple-tv-4k-design-clue.jpg' + url_image
        self.publisherAt = publisherAt
        self.content=content
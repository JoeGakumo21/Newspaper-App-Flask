import unittest
from models import news
News =news.News


class NewsTest(unittest.TestCase):
    '''
    method to test the news class
    '''
    def setUp(self):
        '''
        setup that run before any other method to test the news class
        '''

        self.new_news=News("MacRumors,Deals: Get the Lowest Price on the 2021 32GB Apple TV 4K, Available for $169 ($10 Off),https://images.macrumors.com/t/tzJhmO9DcRnY3jtlKgvHUk2kZfQ=/2500x/https://images.macrumors.com/article-new/2021/04/apple-tv-4k-design-clue.jpg,2021-09-08T17:29:02Z,Today we're tracking the best discount seen to date on the 2021 Apple TV 4K, which provides up to $10 in savings on the 32GB and 64GB models. Starting with the 32GB Apple TV 4K, you can get this mode… [+838 chars]",)

    def test_instance(self):
        '''
        test to check for the instances when created
        '''    
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()
from django.test import TestCase

# Create your tests here.

from django.test import RequestFactory      # RequestFactory：django自身集成的测试套件
from .views import Article


class TestArticleApi(TestCase):

    def setUp(self):
        self.title1 = '测试文章1'
        self.content1="测试文章1测试文章1"
        self.factory = RequestFactory()
        self.article = Article.objects.create(title=self.title1, content=self.content1)
        self.article.save()

    def test_query_article(self):
        request = self.factory.get('/query_article')
        print("request: ", request)


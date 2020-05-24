from django.shortcuts import render
from .models import Article
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.

"""
可以先在后台管理中添加一些文章测试数据
查询文章接口
"""
def query_article(request):
    if request.method == 'GET':
        articles = {}
        # 查询所有文章
        query_articles = Article.objects.all()
        print("query_articles: ", query_articles)
        for article in query_articles:
            articles[article.title] = article.content
        return JsonResponse(
            {
                "status": 200,
                "articles": articles,
                "msg": "查询成功"
            }
        )
        print("request.body: ", request.body)
    else:
        return HttpResponse("请求方法错误")

"""
增加文章接口
"""
def add_article(request):
    if request.method == "POST":
        # 查询当前库中有哪些文章
        articles_title = []
        query_articles = Article.objects.all()
        print("query_articles: ", query_articles)
        for article in query_articles:
            articles_title.append(article.title)
        print("articles_title: ", articles_title)

        print('request.body: ', request.body)
        print('type of request.body: ', type(request.body))
        request_dict = json.loads(request.body)
        print('request_dict: ', request_dict)
        print('type of req_json: ', type(request_dict))
        key_flag = request_dict.get('title') and request_dict.get('content') and len(request_dict) == 2
        print("key_flag: ", key_flag)
        if key_flag:
            title = request_dict['title']
            content = request_dict['content']
            # title返回的是一个list
            # title_exist = Article.objects.filter(title=title)
            print("request_dict[title]", request_dict['title'])
            # print("title_exist: ", title_exist.get('title'))
            # 判断 title 重复（have bug）
            if request_dict['title'] in articles_title:
                return JsonResponse(
                    {
                        "status": 401,
                        "msg": "文章已存在"
                    }
                )
            add_articles = Article(title=title, content=content, status='alive')
            add_articles.save()
            # return HttpResponse(add_articles)
            return JsonResponse(
                {
                    "status": 200,
                    "msg": '添加成功'
                }
            )
        else:
            return JsonResponse(
                {
                    "status": 400,
                    "msg": "参数不正确"
                }
            )
    else:
        print("请求方法错误")


"""
修改文章
"""
def modify_article(request, article_id):
    if request.method == "POST":
        article = Article.objects.get(id=article_id)
        print("article: ", article)
        modify_req = json.loads(request.body)
        print("modify_req: ", modify_req)
        key_flag = modify_req.get('title') and modify_req.get('content') and len(modify_req) == 2

        articles_title = []
        query_articles = Article.objects.all()
        print("query_articles: ", query_articles)
        for article in query_articles:
            articles_title.append(article.title)
        print("articles_title: ", articles_title)

        request_dict = json.loads(request.body)
        request_title = request_dict['title']
        print("request_title: ", request_title)
        if key_flag:
            title = modify_req['title']
            content = modify_req['content']

            # 这块的判断有逻辑上的错误，需要重新找判断条件
            if request_title not in articles_title:
                return JsonResponse({
                    "status": 401,
                    "msg": "文章不存在，无法更新"
                })
            else:
                old_article = Article.objects.get(id=article_id)
                old_article.title = title
                old_article.content = content
                old_article.save()
                return JsonResponse({
                    "status": 200,
                    "msg": "更新成功"
                })
        else:
            return JsonResponse({
                "status": 401,
                "msg": "参数错误"
            })
    else:
        print("请求方法错误")


"""
删除文章
"""
def delete_article(request, article_id):
    if request.method == "DELETE":
        try:
            article = Article.objects.get(id=article_id)
            article.delete()
            return JsonResponse({
                "status": 200,
                "msg": "删除成功"
            })
        except Article.DoesNotExist:
            return JsonResponse({
                "status": 401,
                "msg": "文章不存在，无法删除"
            })
    else:
        return JsonResponse({
            "status": 400,
            "msg": "请求方法错误"
        })
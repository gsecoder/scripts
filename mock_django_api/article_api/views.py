from django.shortcuts import render
from .models import Article
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
import json
# Create your views here.
from .util.get_authorization_info import decode_user_password

"""
接口认证
"""
def user_auth(func):
    def auth(request, *args, **kwargs):
        # 获取 Authorization 并读取用户名和密码
        print("=======request========: ", request.headers.get("Authorization"))
        try:
            print("我进来了")
            authorization = request.headers.get("Authorization")
            username = decode_user_password(authorization)[0]
            print("username: ", username)
            password = decode_user_password(authorization)[1]
            print("password: ", password)

            # 用户鉴权认证
            if username == 'crisimple' and password == '123456':
                print(JsonResponse({
                    "msg": "认证成功"
                }))
                print("<request>: ", request)
                return func(request, *args, **kwargs)
            else:
                return JsonResponse({
                    "status": 402,
                    "msg": "认证失败"
                })
        except Exception:
            return JsonResponse({
                "status": 401,
                "msg": "请先进行身份认证"
            })
    return auth

def index(request):
    request_articles = Article.objects.all()
    articles = {}
    for article in request_articles:
        articles[article] = article.id
    return render(request, 'article/index.html', {'articles': articles})

def index_detail(request, article_id):
    try:
        request_articles = Article.objects.all()
        print("request_articles: ", request_articles)
        articles = {}
        for article in request_articles:
            if article.id == article_id:
                articles[article_id] = article.content
        print("articles", articles)
        print("articles", articles[article_id])
    except Article.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'article/index_detail.html', {'articles': articles[article_id]})

"""
可以先在后台管理中添加一些文章测试数据
查询文章接口
"""
@user_auth
def query(request):
    print("我已经通过了身份认证")
    if request.method == 'GET':
        articles = {}
        articles_list = []
        print(" articles ", articles)
        # 查询所有文章
        query_articles = Article.objects.all()
        print("query_articles========: ", query_articles)
        article_list = []
        i = 0
        for article in query_articles:
            articles = {}
            print("======article======: ", article)
            articles["id"] = article.id
            print("article.id: ", article.id)
            articles["title"] = article.title
            articles["content"] = article.content
            articles["status"] = article.status
            i += 1
            print("articles %s, %s" % (i, articles))
            article_list.append(articles)
            print("articles_inlist: ", article_list)

        # article_list.append(articles_inlist)
        print("type of article_list: ", type(article_list))
        print("article_list: ", article_list)
        return JsonResponse(
            {
                "status": 200,
                "articles": article_list,
                "msg": "查询成功"
            }
        )
        print("request.body: ", request.body)
    else:
        return HttpResponse("请求方法错误")


"""
增加文章接口
"""
@user_auth
def add(request):
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
@user_auth
def update(request, article_id):
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
@user_auth
def delete(request, article_id):
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
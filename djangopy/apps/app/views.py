# Create your views here.

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("app index.")


def user_list(request):
    # 根据App的注册顺序，在每个App下的template目录中寻找
    return render(request, "user/user_list.html")
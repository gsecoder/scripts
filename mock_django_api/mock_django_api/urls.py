"""mock_django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
import sys
from django.contrib import admin
from django.urls import path
from article_api.views import query_article
from article_api.views import add_article
from article_api.views import modify_article
from article_api.views import delete_article

"""
当前路径
"""
current_path = os.path.dirname(__file__)
print("current_path: ", current_path)
# import os
os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('query_article/', query_article, name='query_article'),
    path('add_article/', add_article, name='add_article'),
    path('modify_article/<int:article_id>', modify_article, name='modify_article'),
    path('delete_article/<int:article_id>', delete_article, name='delete_article'),
    path('article/<int:article_id>', modify_article)
]

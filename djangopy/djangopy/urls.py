"""djangopy URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.urls import include

os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})

urlpatterns = [
    # 反向解析的时候根据 namespace 找到各自应用的路由，防止子路由的路由重名反向解析不到
    path('blog/', include(('blog.urls', "blog"), namespace="blog")),
    path('web/', include(('web.urls', "web"), namespace="web")),
    path('admin/', admin.site.urls),
]

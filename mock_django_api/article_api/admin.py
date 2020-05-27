from django.contrib import admin

# Register your models here.

from .models import User, Article

# 告诉管理员在后台将我们编写的应用导入
admin.site.register(User)
admin.site.register(Article)

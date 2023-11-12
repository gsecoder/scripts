from django.contrib import admin
from .models import Grades
from .models import Student
# from .models import StudentManage

# Register your models here.

# 告诉管理员在后台将我们编写的应用导入
admin.site.register(Grades)
admin.site.register(Student)
# com.secoder.admin.site.register(StudentManage)


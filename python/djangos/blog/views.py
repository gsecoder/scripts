from django.http import HttpResponse
from .models import Grades, Student
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Python is a good language")


def detail(request, num, num1):
    return HttpResponse("detail-%s-%s" % (num, num1))


# =================================================================================
# grades的视图
def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()

    # 将数据传递给模板，模板再渲染页面，将渲染好的页面传递给浏览器
    return render(request, "blog/grades.html", {"grades": gradesList})


# student的视图
def student(request):
    # 去模板里取数据
    studentList = Student.objects.all()

    # 将数据传递给模板，模板再渲染页面，将渲染好的页面传递给浏览器
    return render(request, "blog/student.html", {"student": studentList})


# 定义gradeStudent班级下的学生的视图
def gradeStudent(request, num):
    # 获得对应的班级对象
    grade = Grades.objects.get(pk=num)

    # 获得班级下的所有学生
    studentsList = grade.student_set.all()
    return render(request, "blog/student.html", {"student": studentsList})
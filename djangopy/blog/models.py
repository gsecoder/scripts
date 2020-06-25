from django.db import models

# Create your models here.

"""
定义一个模型类，类里面的属性（像gname）会对应数据库表中的一个字段
"""
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField()

    def __str__(self):
        # return "%s-%d-%d" % (self.gname, self.ggirlnum, self.gboynum)
        return self.gname


# 自定义管理类
class StudentManage(models.Manager):
    def get_queryset(self):
        return super(StudentManage, self).get_queryset().filter(isDelete=False)

    def createStudent(self, name, age, gender, content, grade, lt, ct, isd=False):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontent = content
        stu.sgrade = grade
        stu.lastTime = lt
        stu.createTime = ct
        stu.isDelete = isd

        return stu


# 注意：不需要定义主键，生成时自动添加，并且值自动增加
class Student(models.Model):
    # 自定义模型管理器
    stuObj = models.Manager()
    sudObj1 = StudentManage()

    # 定义类的属性
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontent = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)
    # （主键不规定自动生成）一对多，外键写在多的里面
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)

    # 重写对象的返回值
    def __str__(self):
        # return "%s-%d-%s" % (self.sname, self.sage, self.scontent)
        return self.sname

    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now_add=True)

    # 元选项
    # class Mate:
    #     设置的表名
    #     db_table = 'student'
    #     ordering = ['id']

    # 定义一个类方法来创建对象
    @classmethod
    def createStudent(cls, name, age, gender, content, grade, lt, ct, isd=False):
        stu = cls(sname=name, sage=age, sgender=gender, scontent=content, sgrade=grade, lastTime=lt, createTime=ct, isDelete=isd)
        return stu
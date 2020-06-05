from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=180)
    # activate inactive
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    # delete alive
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.title
            # , self.content, self.content, self.status
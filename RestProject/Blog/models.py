from django.db import models

# Create your models here.
class Blog(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    tittle = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,null=True)
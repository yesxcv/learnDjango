from django.db import models
from datetime import  date
from  django import  forms
# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    def __str__(self):
        return self.name

class Author(models.Model):
    name =models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    numbers_of_comments = models.IntegerField(default=0)
    numbers_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)
    def __str__(self):
        return  self.headline


class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)
    def __str__(self):
        return  self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
# models.py
from django.db import models
from django import forms
from django.forms import  ModelForm


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField("Author")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget = forms.Textarea)
    def send_email(self):
        pass

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()

class UploadFileModel(models.Model):
    file = models.FileField(upload_to="upload/")
    title =models.CharField(max_length=123)

class UploadFileModelField(ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ['title','file']
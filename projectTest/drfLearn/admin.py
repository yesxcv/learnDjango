from django.contrib import admin

# Register your models here.
from django.contrib import  admin
from drfLearn.models import  Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author","status","create_date")
    list_filter = ("status",)
    list_per_page = 10

admin.site.register(Article,ArticleAdmin)
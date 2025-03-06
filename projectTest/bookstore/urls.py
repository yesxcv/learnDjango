from django.urls import path,re_path
from bookstore.views import PublisherListView,GreetingView,ArticlesView,UploadFileView,redirectView

urlpatterns = [
    path("publishers/",PublisherListView.as_view()),
    path("greeting/",GreetingView.as_view()),
    path("articles/2003/",ArticlesView.as_view()),
    path("articles/<int:year>/",ArticlesView.as_view(),{"foo":"f123"}),
    re_path(r"^comments/(?:page-(?P<page_number>[0-9]+)/)?$", ArticlesView.as_view()),
    path("upload/",UploadFileView.as_view()),
    path("uploadModel/",UploadFileView.as_view()),
    path("redirect/",redirectView.as_view())

]
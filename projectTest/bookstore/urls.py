from django.urls import path
from bookstore.views import PublisherListView

urlpatterns = [
    path("publishers/",PublisherListView.as_view())
]
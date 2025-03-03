
from django.views.generic import  ListView
from bookstore.models import Publisher

class PublisherListView(ListView):
    model = Publisher
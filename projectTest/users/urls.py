from django.urls import path
from users.views import UserView

urlpatterns = [
    path("createUser/<str:name>",UserView.as_view(),name="createUser")
]
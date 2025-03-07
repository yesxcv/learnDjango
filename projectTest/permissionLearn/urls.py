from django.urls import path
from permissionLearn.views import BlogPostView,UserView

urlpatterns = [
    path("createuser/<str:name>",UserView.as_view()),
    path("perm/<str:type>/", BlogPostView.as_view(),name="perm_withOut_userid"),
    path("perm/<str:type>/<int:userId>/", BlogPostView.as_view(),name="perm_with_userid")
]

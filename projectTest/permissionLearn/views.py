from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType

from blog.models import BlogPost


class UserView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.create_user(
            username=kwargs.get("name"),
            email="123@312.com",
            password="123456",
        )
        return HttpResponse(user.id)


# Create your views here.
class BlogPostView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs.__str__())
        if (kwargs.get("type") == 'create_perm'):
            content_type = ContentType.objects.get_for_model(BlogPost)
            print(Permission.objects.filter(codename="can_publish"))
            Permission.objects.create(codename="can_publish", name="Can Publish Posts", content_type=content_type)
            return HttpResponse("create_success")
        elif (kwargs.get("type") == 'add_perm'):
            user = get_object_or_404(User, pk=kwargs.get("userId"))
            if user is not None:
                hasOne = user.has_perm("blog.can_publish")
                print(hasOne)
                content_type = ContentType.objects.get_for_model(BlogPost)
                print(content_type)
                permission = Permission.objects.get(codename="can_publish", content_type=content_type)
                user.user_permissions.add(permission)
                hasTwo = user.has_perm("blog.can_publish")
                print(hasTwo)
                user = get_object_or_404(User, pk=kwargs.get("userId"))
                hasThree = user.has_perm("blog.can_publish")
                print(hasThree)
                return HttpResponse("done")
            else:
                return HttpResponse("no user")

from django.contrib.auth.models import User
from rest_framework import  authentication
from rest_framework import  exceptions

class ExampleAuthentication(authentication.BasicAuthentication):
    def authenticate(self, request):
        print(request.META)
        username = request.META.get("HTTP_X_USERNAME")
        print(username)
        if not username:
            return  None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")
        return (user,None)
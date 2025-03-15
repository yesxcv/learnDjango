from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import  get_user_model

User = get_user_model()

class MyCustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.filter(Q(username=username)| Q(email=username)).first()
            if user.check_password(password):
                return user
        except Exception as e:
            return None
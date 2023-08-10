from django.contrib.auth.forms import UserChangeForm
from .models import User


class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

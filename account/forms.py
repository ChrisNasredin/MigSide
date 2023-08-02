from django.contrib.auth.forms import UserChangeForm
from .models import User

class UserEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
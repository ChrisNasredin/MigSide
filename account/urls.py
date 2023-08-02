from django.urls import path
from .views import AccountIndex, AccountLogin, AccountLogout, AccountEdit

urlpatterns = [
    path('', AccountIndex.as_view(), name='account_index'),
    # path('register', AccountRegisterView.as_view(), name='register'),
    path('login', AccountLogin.as_view(), name='login'),
    path('edit', AccountEdit.as_view(), name='edit_account'),
    path('logout', AccountLogout.as_view(next_page='/account'), name='logout')
]
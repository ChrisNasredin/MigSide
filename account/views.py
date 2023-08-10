from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .forms import UserEditForm


# Create your views here.

class AccountIndex(LoginRequiredMixin, TemplateView):

    template_name = 'account/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'h1': 'hello'})
        return context

class AccountLogin(LoginView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'

    def get_success_url(self):
        return reverse_lazy('account:account_index')

class AccountLogout(LogoutView):
    pass    

class AccountEdit(LoginRequiredMixin, UpdateView):
    template_name = 'account/edit_account.html'
    form_class = UserEditForm

    def get_object(self, queryset=None):
        return self.request.user
    def get_success_url(sefl):
        return reverse_lazy('account:account_index')
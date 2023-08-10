from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ticket
from .forms import CreateTicketForm



# Create your views here.

class IndexView(LoginRequiredMixin, ListView):
    template_name = 'ticket/index.html'
    model = Ticket
    paginate_by = 10

    def get_queryset(self):
        return Ticket.objects.filter(Q(executor=self.request.user.pk) | Q(execution_department=self.request.user.position))


class CreateTicket(LoginRequiredMixin, CreateView):
    template_name = 'ticket/create_ticket.html'
    model = Ticket
    form_class = CreateTicketForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({'h1': 'Create ticket'})
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class DetailTicket(LoginRequiredMixin, DetailView):
    template_name = 'ticket/detail_ticket.html'
    model = Ticket





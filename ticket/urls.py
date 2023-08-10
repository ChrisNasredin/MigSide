from django.urls import path
from .views import IndexView, CreateTicket, DetailTicket

urlpatterns = [
    path('', IndexView.as_view(), name='ticket_home'),
    path('create', CreateTicket.as_view(), name='create_ticket'),
    path('<int:pk>', DetailTicket.as_view(), name='detail_ticket')
]

from django.shortcuts import render
from django.views.generic import ListView
from gameseek_app.models import Community
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from gameseek_app.models import Client, Community
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView

from .models import Event

#EVENTS

class EventDetailView(DetailView):

    model = Event
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class EventListView(ListView):
    model = Event
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


#COMMUNITIES

class CommunityListView(ListView):
    model = Community
    context_object_name = 'all_communities'

class CommunityDetailView(DetailView):

    model = Community

    context_object_name = 'community'
    queryset = Community.objects.all()

class CommunityClientListView(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.name = get_object_or_404(Community, name=self.kwargs['community'])
        return Client.objects.filter(Community=self.name)

#CLIENTS

class ClientListView(ListView):

    context_object_name = 'client_list'
    queryset = Client.objects.filter(name='client_name')
    template_name = 'gameseek_app/clientes_list.html'


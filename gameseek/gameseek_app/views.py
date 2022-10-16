from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from gameseek_app.models import Community, Client, Game
from .models import Event
#INDEX

def index(request):
    return render(request, "gameseek_app/home.html")
#CLIENTS

class ClientListView(ListView):
    model = Client

class ClientDetailView(DetailView):

    context_object_name = 'client'
    queryset = Client.objects.all()
    
#EVENTS

class EventListView(ListView):
    model = Event
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class EventDetailView(DetailView):
    model = Event
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

#COMMUNITIES

class CommunityListView(ListView):
    model = Community

class CommunityDetailView(DetailView):
    queryset = Community.objects.all()

#GAMES

class GameListView(ListView):
    model = Game

class GameDetailView(DetailView):
    queryset = Game.objects.all()
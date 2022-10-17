from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import *
from django.urls import reverse_lazy
from django.utils import timezone
from gameseek_app.models import *

#INDEX

def index(request):
    return render(request, "gameseek_app/home.html")

#CONTACTO

def contact(request):
    return render(request, "gameseek_app/contacto.html")


#CLIENTS

class ClientListView(ListView):
    model = Client

class ClientDetailView(DetailView):

    context_object_name = 'client'
    queryset = Client.objects.all()

class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'gender', 'language', 'birthday', 'staff', 'moderator']

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name']

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client-list')
    
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

class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'date', 'limit_of_players', 'game', 'description', 'language']

class EventUpdateView(UpdateView):
    model = Event
    fields = ['name']

class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('event-list')

#COMMUNITIES

class CommunityListView(ListView):
    model = Community

class CommunityDetailView(DetailView):
    queryset = Community.objects.all()

class CommunityCreateView(CreateView):
    model = Community
    fields = ['name', 'description', 'game', 'number_of_players']

class CommunityUpdateView(UpdateView):
    model = Community
    fields = ['name']

class CommunityDeleteView(DeleteView):
    model = Community
    success_url = reverse_lazy('community-list')

#GAMES

class GameListView(ListView):
    model = Game

class GameDetailView(DetailView):
    queryset = Game.objects.all()

class GameCreateView(CreateView):
    model = Game
    fields = ['name', 'description', 'category']

class GameUpdateView(UpdateView):
    model = Game
    fields = ['name']

class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy('game-list')
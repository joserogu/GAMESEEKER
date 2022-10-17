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
    queryset = Client.objects.all()
    context_object_name = 'client'

class ClientUpdateView(UpdateView):
    queryset = Client.objects.all()
    fields = ['name', 'email', 'gender', 'language', 'birthday', 'staff', 'moderator']

class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'gender', 'language', 'birthday', 'staff', 'moderator']

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

class EventUpdateView(UpdateView):
    queryset = Event.objects.all()
    fields = ['name', 'date', 'limit_of_players', 'game', 'description', 'language']

class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'date', 'limit_of_players', 'game', 'description', 'language']

class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('event-list')

#COMMUNITIES

class CommunityListView(ListView):
    model = Community

class CommunityDetailView(DetailView):
    queryset = Community.objects.all()

class CommunityUpdateView(UpdateView):
    queryset = Community.objects.all()
    fields = ['name', 'description', 'game', 'number_of_players']    

class CommunityCreateView(CreateView):
    model = Community
    fields = ['name', 'description', 'game', 'number_of_players']

class CommunityDeleteView(DeleteView):
    model = Community
    success_url = reverse_lazy('community-list')

#GAMES

class GameListView(ListView):
    model = Game

class GameDetailView(DetailView):
    queryset = Game.objects.all()

class GameUpdateView(UpdateView):
    queryset = Game.objects.all()
    fields = ['name', 'description', 'category']

class GameCreateView(CreateView):
    model = Game
    fields = ['name', 'description', 'category']

class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy('game-list')
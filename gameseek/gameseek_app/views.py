from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy
from django.utils import timezone
from gameseek_app.models import *
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.contrib.auth.forms import AuthenticationForm

#DEFAULT VIEW

class DefaultView(TemplateView):
    template_name="gameseek_app/inicio.html"

#FUNCIÓN REGISTER

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/accounts/register.html", context={"register_form":form})

#INDEX

def index(request):
    return render(request, "gameseek_app/inicio.html")

#CONTACTO

def contact(request):
    return render(request, "gameseek_app/contacto.html")


#CLIENTS

class ClientListView(ListView):
    model = Client

class ClientDetailView(UserPassesTestMixin, DetailView):
    queryset = Client.objects.all()
    context_object_name = 'client'
    def test_func(self):
        try:
            return Client.objects.get(pk=self.request.user.pk)==Client.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class ClientUpdateView(UserPassesTestMixin, UpdateView):
    queryset = Client.objects.all()
    fields = ['username', 'email', 'gender', 'language', 'birthday']
    template_name="gameseek_app/client_form.html"
    def test_func(self):
        try:
            return Client.objects.get(pk=self.request.user.pk)==Client.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class ClientCreateView(CreateView):
    model = Client
    form_class=NewUserForm
    template_name="registration/register.html"

class ClientDeleteView(UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('gmsk:client-list')
    template_name="gameseek_app/client_confirm_delete.html"
    def test_func(self):
        try:
            return Client.objects.get(pk=self.request.user.pk)==Client.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False
    
#EVENTS

class EventListView(ListView):
    model = Event

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

class EventUpdateView(UserPassesTestMixin, UpdateView):
    queryset = Event.objects.all()
    fields = ['name', 'date', 'limit_of_players', 'game', 'description', 'language']
    def test_func(self):
        try:
            return Event.objects.get(pk=self.request.user.pk)==Event.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class EventCreateView(UserPassesTestMixin, CreateView):
    model = Event
    fields = ['name', 'date', 'limit_of_players', 'game', 'description', 'language']
    def test_func(self):
        try:
            return Event.objects.get(pk=self.request.user.pk)==Event.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class EventDeleteView(UserPassesTestMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('gmsk:event-list')
    def test_func(self):
        try:
            return Event.objects.get(pk=self.request.user.pk)==Event.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

#COMMUNITIES

class CommunityListView(ListView):
    model = Community

class CommunityDetailView(DetailView):
    queryset = Community.objects.all()

class CommunityUpdateView(UpdateView):
    queryset = Community.objects.all()
    fields = ['name', 'description', 'game', 'number_of_players', 'img'] 
    def test_func(self):
        try:
            return Community.objects.get(pk=self.request.user.pk)==Community.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False   

class CommunityCreateView(CreateView):
    model = Community
    fields = ['name', 'description', 'game', 'number_of_players', 'img']

class CommunityDeleteView(DeleteView):
    model = Community
    success_url = reverse_lazy('gmsk:community-list')
    def test_func(self):
        try:
            return Community.objects.get(pk=self.request.user.pk)==Community.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False  

#GAMES

class GameListView(ListView):
    model = Game

class GameDetailView(DetailView):
    queryset = Game.objects.all()
    template_name = "gameseek_app/game_detail.html"

class GameUpdateView(UpdateView):
    queryset = Game.objects.all()
    fields = ['name', 'description', 'category']

class GameCreateView(CreateView):
    model = Game
    fields = ['name', 'description', 'category']

class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy('gmsk:games-list')
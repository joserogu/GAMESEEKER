from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy
from django.utils import timezone
from gameseek_app.models import *
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm
from django.db.models import Q

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.contrib.auth.forms import AuthenticationForm

#DEFAULT VIEW

class DefaultView(TemplateView):
    template_name="gameseek_app/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comunidades']=Community.objects.all()[0:2]
        context['eventos']=Event.objects.all()[0:3]
        return context

class search(ListView):
    model = Community
    template_name="gameseek_app/search.html"
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list=Community.objects.filter(Q(name__icontains=query))
        return object_list

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comunidades']=Community.objects.filter(cliente=self.request.user.pk)
        return context

    def test_func(self):
        try:
            return Client.objects.get(pk=self.request.user.pk)==Client.objects.get(pk=self.kwargs.get("pk"))
        except:
            return False

class ClientUpdateView(UserPassesTestMixin, UpdateView):
    queryset = Client.objects.all()
    fields = ['username', 'email', 'gender', 'language', 'birthday', 'cargo']
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
    success_url = reverse_lazy('gmsk:clients-list')

class ClientDeleteView(UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('gmsk:clients-list')
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
        context['comunidades']=Community.objects.get(pk=self.request.user.pk)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class EventUpdateView(UserPassesTestMixin, UpdateView):
    queryset = Event.objects.all()
    fields = ['name', 'date', 'limit_of_players', 'description', 'language','comunidad']
    def test_func(self):
        try:
            return self.request.user.is_superuser
        except:
            return False

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'date', 'limit_of_players', 'description', 'language', 'comunidad']

class EventDeleteView(UserPassesTestMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('gmsk:events-list')
    def test_func(self):
        try:
            return self.request.user.is_superuser
        except:
            return False

#COMMUNITIES

class CommunityListView(ListView):
    model = Community
    

class CommunityDetailView(LoginRequiredMixin, DetailView):
    queryset = Community.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos']=Event.objects.filter(comunidad=self.kwargs.get("pk"))
        return context

class CommunityUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Community
    queryset = Community.objects.all()
    fields = ['name', 'description', 'number_of_players', 'img', 'juegos', 'cliente'] 
    def test_func(self): 
        try:
            return self.request.user.is_superuser
        except:
            return False   

class CommunityCreateView(LoginRequiredMixin, CreateView):
    model = Community
    fields = ['name', 'description', 'number_of_players', 'img', 'juegos', 'cliente']

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('gmsk:communitys-list'))

class CommunityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Community
    queryset = Community.objects.all()
    success_url = reverse_lazy('gmsk:communitys-list')
    def test_func(self): 
        try:
            return self.request.user.is_superuser
        except:
            return False
        
        

#GAMES

class GameListView(LoginRequiredMixin, ListView):
    model = Game

class GameDetailView(LoginRequiredMixin, DetailView):
    queryset = Game.objects.all()
    template_name = "gameseek_app/game_detail.html"

class GameUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Game.objects.all()
    fields = ['name', 'description', 'category']

class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['name', 'description', 'category']

class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = reverse_lazy('gmsk:games-list')
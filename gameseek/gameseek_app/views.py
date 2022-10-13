from django.shortcuts import render
from django.views.generic import ListView
from gameseek_app.models import Community
from django.views.generic import DetailView
from gameseek_app.models import Client


class CommunityListView(ListView):
    model = Community
    context_object_name: "my_favourite_game"

class CommunityDetailView(DetailView):

    model = Community

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['client_list'] = Client.objects.all()
        return context

class ClientListView(ListView):

    context_object_name = 'client_list'
    queryset = Client.objects.filter(name='Clientes activos')
    template_name = 'gameseek_app/clientes_list.html'
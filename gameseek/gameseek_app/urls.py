from django.contrib import admin
from django.urls import path
from gameseek_app.views import *
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('', DefaultView.as_view(), name="home"),
    
    #CLIENTES
    
    path("clients/", ClientListView.as_view(), name="clients-list"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="clients-detail"),
    path("register/", ClientCreateView.as_view(), name='clients-add'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='clients-update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='clients-delete'),

    #EVENTOS

    path('eventos/', EventListView.as_view(), name="events-list"),
    path('eventos/<int:pk>/', EventDetailView.as_view(), name='events-detail'),
    path("eventos/add/", EventCreateView.as_view(), name='events-add'),
    path('eventos/<int:pk>/edit/', EventUpdateView.as_view(), name='events-update'),
    path('eventos/<int:pk>/delete/', EventDeleteView.as_view(), name='events-delete'),

    #COMUNIDADES

    path('comunidades/', CommunityListView.as_view(), name="communitys-list"),
    path('comunidades/<int:pk>/', CommunityDetailView.as_view(), name='communitys-detail'),
    path("comunidades/add/", CommunityCreateView.as_view(), name='communitys-add'),
    path('comunidades/<int:pk>/edit/', CommunityUpdateView.as_view(), name='communitys-update'),
    path('comunidades/<int:pk>/delete/', CommunityDeleteView.as_view(), name='communitys-delete'),

    #JUEGOS

    path('juegos/', GameListView.as_view(), name="games-list"),
    path('juegos/<int:pk>/', GameDetailView.as_view(), name='games-detail'),
    path("juegos/add/", GameCreateView.as_view(), name='games-add'),
    path('juegos/<int:pk>/edit/', GameUpdateView.as_view(), name='games-update'),
    path('juegos/<int:pk>/delete/', GameDeleteView.as_view(), name='games-delete'),

]
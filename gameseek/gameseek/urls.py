"""gameseek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gameseek_app.views import *
from django.conf.urls.static import static
from django.conf import settings
from gameseek_app.api import *



urlpatterns = [
    path('', index),
    path('contacto/', contact),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),

    #CLIENTES
    
    path("clients/", ClientListView.as_view(), name="clients-list"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="clients-detail"),
    path("register/", ClientCreateView.as_view(), name='client-add'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),

    #EVENTOS

    path('eventos/', EventListView.as_view(), name="events-list"),
    path('eventos/<int:pk>/', EventDetailView.as_view(), name='events-detail'),
    path("eventos/add/", EventCreateView.as_view(), name='event-add'),
    path('eventos/<int:pk>/edit/', EventUpdateView.as_view(), name='event-update'),
    path('eventos/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),

    #COMUNIDADES

    path('comunidades/', CommunityListView.as_view(), name="communitys-list"),
    path('comunidades/<int:pk>/', CommunityDetailView.as_view(), name='communitys-detail'),
    path("comunidades/add/", CommunityCreateView.as_view(), name='community-add'),
    path('comunidades/<int:pk>/edit/', CommunityUpdateView.as_view(), name='community-update'),
    path('comunidades/<int:pk>/delete/', CommunityDeleteView.as_view(), name='community-delete'),

    #JUEGOS

    path('juegos/', GameListView.as_view(), name="games-list"),
    path('juegos/<int:pk>/', GameDetailView.as_view(), name='games-detail'),
    path("juegos/add/", GameCreateView.as_view(), name='game-add'),
    path('juegos/<int:pk>/edit/', GameUpdateView.as_view(), name='game-update'),
    path('juegos/<int:pk>/delete/', GameDeleteView.as_view(), name='game-delete'),

    #API
    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
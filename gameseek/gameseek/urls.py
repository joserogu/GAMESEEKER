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
from django.urls import path
from django.views.generic.base import TemplateView
from gameseek_app import views
from gameseek_app.views import *



urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path("clients/", ClientListView.as_view(), name="client-list"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client-detail"), 
    path('eventos/', EventListView.as_view(), name="event-list"),
    path('eventos/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('comunidades/', CommunityListView.as_view(), name="community-list"),
    path('comunidades/<int:pk>/', CommunityDetailView.as_view(), name='community-detail'),
    path('juegos/', GameListView.as_view(), name="game-list"),
    path('juegos/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
]

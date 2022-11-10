from gameseek_app.models import *
from rest_framework import routers,serializers, viewsets

# Cliente

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['username', 'email', 'gender', 'language', 'birthday']

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Eventos

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'date', 'limit_of_players', 'game', 'description', 'language']

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Comunidades

class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = ['name', 'description', 'game', 'number_of_players', 'img']

class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

# Juegos

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['name', 'description', 'category']

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

#REGISTER
api = routers.DefaultRouter()
api.register(r'clientes', ClientViewSet)
api.register(r'eventos', EventViewSet)
api.register(r'comunidades', CommunityViewSet)
api.register(r'juegos', GameViewSet)
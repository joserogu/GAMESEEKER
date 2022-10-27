from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from django.contrib.auth.models import User, AbstractUser



# Register your models here.

admin.site.register(Client)
admin.site.register(Event)
admin.site.register(Community)
admin.site.register(Game)


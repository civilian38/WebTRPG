from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TRPGUser

admin.site.register(TRPGUser, UserAdmin)
from django.contrib import admin

# Register your models here.

from rest_framework.authtoken.admin import TokenAdmin
from .models import Hero


TokenAdmin.raw_id_fields = ['user']

admin.site.register(Hero)
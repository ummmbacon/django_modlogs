# modlogs/admin.py
from django.contrib import admin
from .models import ModLog

admin.site.register(ModLog)

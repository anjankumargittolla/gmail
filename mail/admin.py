from django.contrib import admin

"""Models are imported from app models to register in admin panel"""
from .models import Registration, Mails

# Register your models here.
admin.site.register(Registration)
admin.site.register(Mails)

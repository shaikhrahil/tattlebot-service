from django.contrib import admin

from .models import Observer


@admin.register(Observer)
class ObserverAdmin(admin.ModelAdmin):
    pass

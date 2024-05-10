from django.contrib import admin

from .models import Station, Train

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'origin', 'destination', 'departure_time', 'arrival_time')

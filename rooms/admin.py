from django.contrib import admin
from rooms.models import Room, Message, Shared_file
# Register your models here.

@admin.register(Room)
class RoomModelAdmin(admin.ModelAdmin):
    list_display =  ['id', 'name', 'slug']


@admin.register(Message)
class RoomModelAdmin(admin.ModelAdmin):
    list_display =  ['id', 'room', 'user', 'content', 'date_added']

@admin.register(Shared_file)
class Shared_fileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'uploader', 'room']

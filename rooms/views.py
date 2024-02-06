from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from rooms.models import Room, Message, Shared_file
from django.contrib.auth.decorators import login_required
# from .forms import FielUploadForm
# Create your views here.

@login_required
def rooms(request):
    r = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': r})

def userroom(request, slug):
    ur = Room.objects.get(slug=slug)
    mesasges = Message.objects.filter(room=ur)[0:30]
    images = Shared_file.objects.filter(room=ur)
    # for i in images:
    #     k = i.file.split('blob:http//127.0.0.1/' + [20: ])
    return render(request, 'room/room.html', {'room': ur, 'messages': mesasges, 'images': images})



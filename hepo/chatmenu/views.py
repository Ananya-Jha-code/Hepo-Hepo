from django.shortcuts import render, redirect
from .models import Room, Messages
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Count


def chat_menu(request):
    users = Messages.objects.values('username').distinct()
    val = dict()
    for u in users:
        cc = Messages.objects.filter(username=u['username']).count()
        val[u['username']] = cc
    rooms = Room.objects.all()
    return render(request, 'chatmenu.html', {
        'rooms': rooms,
        'users': users,
        'val': val
    })


def room(request, room):
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']

    if Room.objects.filter(name=room).exists():
        messages.error(request, 'the room already exists')
        return redirect('/login/chatmenu')
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/login/chatmenu/' + room)








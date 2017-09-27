from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..authentication_app.models import User
from models import *
from django.contrib import messages
import bcrypt
def index(request):
    if 'Email' not in request.session:
        messages.error(request, 'You must be logged in to visit the cars pages')
        return redirect('/')
    thisUser = User.objects.get(Email=request.session['Email'])
    otherUsers = User.objects.exclude(Email=request.session['Email'])
    myCars = Car.objects.filter(OwnerId=thisUser.id).all()
    context = {
        'user' : thisUser,
        'otherUsers': otherUsers,
        'myCars': myCars,
        }
    return render(request, "Cars_app/index.html", context)

def add(request):
    if 'Email' not in request.session:
        messages.error(request, 'You must be logged in to visit the add cars pages')
        return redirect('/')
    thisUser = User.objects.get(Email=request.session['Email'])
    context = { 'thisuser': thisUser }
    return render(request, "Cars_app/add.html", context)

def createcar(request):
    if 'Email' not in request.session:
        messages.error(request, 'You must be logged in to create a car')
        return redirect('/')
    result = Car.objects.Creator(request.POST)
    if len(result['errors']) == 0:
        return redirect('/cars')
    else:
        messages.error(request, "Validation failed")
        for anError in result['errors']:
            messages.error(request, anError)
        return redirect('/cars/add')

def show(request, Id):
    if 'Email' not in request.session:
        messages.error(request, 'You must be logged in to visit a user cars page')
        return redirect('/')
    try:
        thisUser = User.objects.get(id=Id)
    except Exception as e:
        messages.error(request, 'User with the ID of {} does not exist.'.format(Id))
        return redirect('/cars')
    if None == thisUser:
        messages.error(request, 'User with the ID of {} does not exist.'.format(Id))
        return redirect('/cars')
    context = { 'thisUser': thisUser }
    return render(request, "Cars_app/show.html", context)

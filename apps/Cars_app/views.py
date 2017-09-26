from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..authentication_app.models import *
from models import *
from django.contrib import messages
import bcrypt
def index(request):
    if 'Email' not in request.session:
        messages.error(request, 'You must be logged in to visit the cars pages')
        return redirect('/')
    thisUser = User.objects.get(Email=request.session['Email'])
    otherUsers = User.objects.exclude(Email=request.session['Email'])

    print "otherUsers = ",  otherUsers, "%"*80

    allCars = Car.objects.all()
    myCars = Car.objects.filter(OwnerId=thisUser.id).all()
    context = {
        'user' : thisUser,
        'otherUsers': otherUsers,
        'myCars': myCars,
        'allCars' : allCars, 
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

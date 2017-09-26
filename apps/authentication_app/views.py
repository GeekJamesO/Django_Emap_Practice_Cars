from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

def index(request):
    context = { }
    return render(request, "authentication_app/index.html", context)

def register(request):
    result = User.objects.Validate(request.POST)
    if result['status'] == True:
        thisUser = User.objects.Creator(request.POST)
        messages.info(request, "Successfully created user '{} {}'.".format(thisUser.First_Name, thisUser.Last_Name))
    else:
        for anError in result['errors']:
            messages.error(request, anError)
    return redirect("/")

def login(request):
    result = User.objects.LoginVal(request.POST)
    if result['status'] == True:
        messages.info(request, "Successfully logged in user '{} {}'.".format(result['user'].First_Name, result['user'].Last_Name))
        request.session['Email']=result['user'].Email
        request.session['First_Name']=result['user'].First_Name
        request.session['Last_Name']=result['user'].Last_Name
        # return redirect ("/dashboard")
        return redirect ("/cars/")
    else:
        messages.error(request, "Validation failed")
        for anError in result['errors']:
            messages.error(request, anError)
        return redirect("/")

def dashboard(request):
    if 'Email' not in request.session:
        messages.error(request, 'you must be logged in to visit the dashboard.')
        return redirect('/')
    return render(request, "cars/dashboard.html")

def logoff(request):
        messages.info(request, "Successfully logged out user.")
        request.session.flush()
        return redirect ("/")

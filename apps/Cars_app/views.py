from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import bcrypt
def index(request):
    context = { }
    return render(request, "Cars_app/index.html", context)

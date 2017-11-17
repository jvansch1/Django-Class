# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import random

from django.shortcuts import render

# Create your views here.

def home(request):
    num = random.randint(0,1000000)
    return render(request, "home.html", { "bool_item": False, "num": num, "some_list": [1,2,3,4] })

def contact(request):
    num = random.randint(0,1000000)
    return render(request, "contact.html", { "bool_item": False, "num": num, "some_list": [1,2,3,4] })

def about(request):
    num = random.randint(0,1000000)
    return render(request, "about.html", { "bool_item": False, "num": num, "some_list": [1,2,3,4] })

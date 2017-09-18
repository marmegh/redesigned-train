# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Render html page that displays time

def index(request):
    context = {
        'time': strftime("%b %d, %Y %I:%M %p", gmtime())
    }
    return render(request, 'timedisplay/time.html', context)
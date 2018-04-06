# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def new(request):
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
		print "*"*50
		print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
		print "*"*50
		return redirect("/")
	else:

def show(request, number):
    response = 'placeholder to display blog '+number 
    return HttpResponse(response)

def edit(request, number):
    response = 'placeholder to edit blog '+number 
    return HttpResponse(response)

def destroy(request, number):
    print 'this was destroyed ' + number
    return redirect('/')
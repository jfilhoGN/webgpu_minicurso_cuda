from django.shortcuts import render, HttpResponse
from django.template import loader

def home(request):
	return render(request, 'home.html')

def login(request):
	return render(request, 'login.html')
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from django.views.decorators.http import require_POST


def home(request):
	return render(request, 'home.html')

def login(request):
	return render(request, 'login.html')


# @require_POST
# def entrar(request):
#     usuario_aux = User.objects.get(email=request.POST['email'])
#     usuario = authenticate(username=usuario_aux.username,
#                            password=request.POST["senha"])
#     if usuario is not None:
#         login(request, usuario)
#         return HttpResponseRedirect('/home/')

#     return HttpResponseRedirect('/')

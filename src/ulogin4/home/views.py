from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


def index(request):
    return render_to_response('index.html')

def Login(request):
    next = request.GET.get('next', '/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Account is not active at the moment.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "index.html", {'next': next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

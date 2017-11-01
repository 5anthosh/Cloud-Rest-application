from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Api.models import Channel, Field


def user_create(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return HttpResponseRedirect('/user/')
    return render(request, "Api/index.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            print("d")
            if user.is_active:
                login(request, user)
                print("actibe")
                return HttpResponseRedirect('/user/')
            else:
                return HttpResponse("not active")
        else:
            HttpResponse("incorrect")
    return render(request, "Api/login.html")


@login_required(login_url='/user/login/')
def home(request):
    user = request.user
    token = Token.objects.get(user=user)
    a = []
    channels = Channel.objects.filter(user=user)
    for channel in channels:
        fields = Field.objects.filter(channel=channel)
        a.append((channel, fields))
    return render(request, "Api/user_iu.html", {"token": token.key, 'data': a, 'user':request.user.username})


@login_required(login_url='/user/login/')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/user/login/')

# Create your views here.

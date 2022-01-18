from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/signin")
def index(request):
    return render(request, 'frontend/home.html')


def playlist(request):
    return render(request, 'frontend/playlist.html')

def signup(request):
    return render(request, 'frontend/signup.html')

def signin(request):
    return render(request, 'frontend/signin.html')

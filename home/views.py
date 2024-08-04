from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'home.html')

def dashboard(request):
    return render(request, "pages/dashboard.html")

def login(request):
    return render(request, "accounts/sign-in.html")
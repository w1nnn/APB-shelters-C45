from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def index(request):

    return render(request, 'home.html')

def dashboard(request):
    return render(request, "pages/dashboard.html")

def login(request):
    return render(request, "accounts/sign-in.html")

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'accounts/sign-in.html', {'error': "Invalid username or password."}) 

def shelter(request):
    return render(request, "pages/shelter.html")        
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Shelter

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
    shelters = Shelter.objects.all()
    return render(request, "pages/shelter.html", {'shelters': shelters}) 

def shelter_add(request):
    return render(request, "pages/shelter-add.html")       

def save_shelter(request):
    if request.method == 'POST':
        nama_bangunan = request.POST.get('nama_bangunan')
        latitude_longitude = request.POST.get('kordinat')
        alamat = request.POST.get('alamat')
        
        Shelter.objects.create(
            nama_bangunan=nama_bangunan,
            latitude_longitude=latitude_longitude,
            alamat=alamat
        )
        messages.success(request, "Data berhasil disimpan.")
        return redirect('/shelter')
        
    return render(request, 'page/shelter.html') 

def delete_shelter(request, id):
    Shelter.objects.filter(id=id).delete()
    messages.success(request, "Data berhasil dihapus.")
    return redirect('/shelter')

def edit_shelter(request, id):
    shelter = Shelter.objects.get(id=id)
    return render(request, 'pages/shelter-edit.html', {'shelter': shelter})

def update_shelter(request, id):
    if request.method == 'POST':
        nama_bangunan = request.POST.get('nama_bangunan')
        latitude_longitude = request.POST.get('kordinat')
        alamat = request.POST.get('alamat')
        
        shelter = Shelter.objects.get(id=id)
        shelter.nama_bangunan = nama_bangunan
        shelter.latitude_longitude = latitude_longitude
        shelter.alamat = alamat
        shelter.save()
        messages.success(request, "Data berhasil diubah.")
        return redirect('/shelter')
        
    return render(request, 'pages/shelter-edit.html')
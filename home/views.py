from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Shelter
from .models import User
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

        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user'] = user.id
            messages.error(request, 'Login berhasil')
            return redirect('/dashboard')
        else:
            messages.error(request, 'Username atau password salah')
            return redirect('/login')


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
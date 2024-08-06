from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Shelter
from .models import User
from .models import Kriteria
# main
def index(request):
    return render(request, 'home.html')

def dashboard(request):
    kriteria_count = Kriteria.objects.count()
    shelter_count = Shelter.objects.count()
    context = {
        'kriteria_count': kriteria_count,
        'shelter_count': shelter_count,
    }
    return render(request, "pages/dashboard.html", context)

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

# Shelter
def shelter(request):
    shelters = Shelter.objects.all()
    return render(request, "pages/shelter.html", {'shelters': shelters}) 

def shelter_add(request):
    kriteria_atap = Kriteria.objects.filter(nama_kriteria='ATAP')
    kriteria_rangka_atap = Kriteria.objects.filter(nama_kriteria='RANGKA ATAP')
    kriteria_kolom_bangunan = Kriteria.objects.filter(nama_kriteria='KOLOM BANGUNAN')

    context = {
        'kriteria_atap': kriteria_atap,
        'kriteria_rangka_atap': kriteria_rangka_atap,
        'kriteria_kolom_bangunan': kriteria_kolom_bangunan,
    }

    return render(request, "pages/shelter-add.html", context)      

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Shelter

def save_shelter(request):
    if request.method == 'POST':
        nama_bangunan = request.POST.get('nama_bangunan')
        latitude_longitude = request.POST.get('kordinat')
        alamat = request.POST.get('alamat')
        atap = request.POST.get('atap')
        rangka_atap = request.POST.get('rangka_atap')
        kolom_bangunan = request.POST.get('kolom_bangunan')
        status = request.POST.get('status')
        
        
        if Shelter.objects.filter(latitude_longitude=latitude_longitude).exists():
            messages.error(request, "Lokasi dengan koordinat ini sudah ada.")
            return redirect('/shelter')

        Shelter.objects.create(
            nama_bangunan=nama_bangunan,
            latitude_longitude=latitude_longitude,
            alamat=alamat,
            atap=atap,
            rangka_atap=rangka_atap,
            kolom_bangunan=kolom_bangunan,
            status=status
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
    kriteria_atap = Kriteria.objects.filter(nama_kriteria='ATAP')
    kriteria_rangka_atap = Kriteria.objects.filter(nama_kriteria='RANGKA ATAP')
    kriteria_kolom_bangunan = Kriteria.objects.filter(nama_kriteria='KOLOM BANGUNAN')
    
    context = {
        'shelter': shelter,
        'kriteria_atap': kriteria_atap,
        'kriteria_rangka_atap': kriteria_rangka_atap,
        'kriteria_kolom_bangunan': kriteria_kolom_bangunan,
    }
    
    return render(request, 'pages/shelter-edit.html', context)

def update_shelter(request, id):
    shelter = get_object_or_404(Shelter, id=id)

    if request.method == 'POST':
        # Ambil data dari form
        shelter.nama_bangunan = request.POST.get('nama_bangunan')
        shelter.latitude_longitude = request.POST.get('kordinat')
        shelter.alamat = request.POST.get('alamat')
        shelter.rangka_atap = request.POST.get('rangka_atap')
        shelter.kolom_bangunan = request.POST.get('kolom_bangunan')
        shelter.status = request.POST.get('status')

        # Simpan perubahan ke database
        shelter.save()

        messages.success(request, "Data berhasil diubah.")
        return redirect('/shelter')  # Ganti dengan nama URL yang sesuai

    # Jika metode request bukan POST, render halaman edit dengan data yang ada
    context = {
        'shelter': shelter,
        'kriteria_rangka_atap': Kriteria.objects.filter(nama_kriteria='RANGKA ATAP'),
        'kriteria_kolom_bangunan': Kriteria.objects.filter(nama_kriteria='KOLOM BANGUNAN'),
    }
    return render(request, 'pages/shelter-edit.html', context)

# Kriteria
def kriteria(request):
    return render(request, 'pages/kriteria.html', {'kriterias': Kriteria.objects.all()})

def kriteria_add(request):
    return render(request, 'pages/kriteria-add.html')

def save_kriteria(request):
    if request.method == 'POST':
        nama_kriteria = request.POST.get('nama_kriteria')
        sub_kriteria = request.POST.get('sub_kriteria')
        bobot = request.POST.get('bobot')

        if Kriteria.objects.filter(nama_kriteria=nama_kriteria, sub_kriteria=sub_kriteria, bobot=bobot).exists():
            messages.error(request, "Data dengan kriteria yang sama sudah ada.")
            return redirect('/kriteria')

        Kriteria.objects.create(
            nama_kriteria=nama_kriteria,
            sub_kriteria=sub_kriteria,
            bobot=bobot
        )
        messages.success(request, "Data berhasil disimpan.")
        return redirect('/kriteria')

def delete_kriteria(request, id):
    Kriteria.objects.filter(id=id).delete()
    messages.success(request, "Data berhasil dihapus.")
    return redirect('/kriteria')

def edit_kriteria(request, id):
    kriteria = Kriteria.objects.get(id=id)
    return render(request, 'pages/kriteria-edit.html', {'kriteria': kriteria})


def update_kriteria(request, id):
    if request.method == 'POST':
        nama_kriteria = request.POST.get('nama_kriteria')
        sub_kriteria = request.POST.get('sub_kriteria')
        bobot = request.POST.get('bobot')

        kriteria = Kriteria.objects.get(id=id)
        kriteria.nama_kriteria = nama_kriteria
        kriteria.sub_kriteria = sub_kriteria
        kriteria.bobot = bobot
        kriteria.save()
        messages.success(request, "Data berhasil diubah.")
        return redirect('/kriteria')
        
    return render(request, 'pages/kriteria-edit.html')

        

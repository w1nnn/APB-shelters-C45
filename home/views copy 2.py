from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Shelter
from .models import User
from .models import Kriteria
# D3
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from django.conf import settings
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import os

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
        shelter.nama_bangunan = request.POST.get('nama_bangunan')
        shelter.latitude_longitude = request.POST.get('kordinat')
        shelter.alamat = request.POST.get('alamat')
        shelter.rangka_atap = request.POST.get('rangka_atap')
        shelter.kolom_bangunan = request.POST.get('kolom_bangunan')
        shelter.status = request.POST.get('status')

        shelter.save()

        messages.success(request, "Data berhasil diubah.")
        return redirect('/shelter')  # Ganti dengan nama URL yang sesuai

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

        
# Decision Tree
def analyze_data(request):
    try:
        # Set backend non-GUI untuk Matplotlib
        import matplotlib
        matplotlib.use('Agg')
        
        # Load data
        training_file_path = os.path.join(settings.BASE_DIR, 'static/data/data_traning.xlsx')
        testing_file_path = os.path.join(settings.BASE_DIR, 'static/data/data_testing.xlsx')

        # Check if files exist
        if not os.path.exists(training_file_path):
            raise FileNotFoundError(f"Training file not found: {training_file_path}")
        if not os.path.exists(testing_file_path):
            raise FileNotFoundError(f"Testing file not found: {testing_file_path}")

        # Read Excel files
        df = pd.read_excel(training_file_path, engine='openpyxl')
        dt = pd.read_excel(testing_file_path, engine='openpyxl')

        # Map categorical values
        atap_mapping = {'Seng': 1, 'Asbes': 2, 'Genteng': 3, 'Cor': 4}
        df['ATAP'] = df['ATAP'].map(atap_mapping).fillna(0)
        dt['ATAP'] = dt['ATAP'].map(atap_mapping).fillna(0)

        rangka_atap_mapping = {'Kayu': 1, 'Baja ringan': 1, 'Besi': 2, 'Beton': 3}
        df['RANGKA ATAP'] = df['RANGKA ATAP'].map(rangka_atap_mapping).fillna(0)
        dt['RANGKA ATAP'] = dt['RANGKA ATAP'].map(rangka_atap_mapping).fillna(0)

        kolom_bangunan_mapping = {'Kayu': 1, 'Baja ringan': 1, 'Besi': 2, 'Beton berulang': 3}
        df['KOLOM BANGUNAN'] = df['KOLOM BANGUNAN'].map(kolom_bangunan_mapping).fillna(0)
        dt['KOLOM BANGUNAN'] = dt['KOLOM BANGUNAN'].map(kolom_bangunan_mapping).fillna(0)

        decision_mapping = {'Secure': 1, 'Un-Secure': 0}
        df['DECISION'] = df['DECISION'].map(decision_mapping)
        dt['DECISION'] = dt['DECISION'].map(decision_mapping)

        features = ['ATAP', 'RANGKA ATAP', 'KOLOM BANGUNAN']
        xTrain = df[features]
        yTrain = df['DECISION']

        # Train Decision Tree model
        dtree = DecisionTreeClassifier()
        dtree = dtree.fit(xTrain, yTrain)

        # Accuracy calculation
        xTesting = dt[features]
        yTesting = dt['DECISION']

        hasilPrediksi = dtree.predict(xTesting)
        hasilPrediksi_label = ['Secure' if pred == 1 else 'Un-Secure' for pred in hasilPrediksi]

        accuracy = metrics.accuracy_score(yTesting, hasilPrediksi)

        # Generate the decision tree plot
        plt.figure(figsize=(20,20), facecolor='w')
        tree.plot_tree(dtree, feature_names=features)

        # Save plot to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        # Encode the plot to base64
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

        # Prepare context
        context = {
            'image_base64': image_base64,
            'accuracy': accuracy,
            'predictions': hasilPrediksi_label,
        }

        return render(request, 'analyze.html', context)
    
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)
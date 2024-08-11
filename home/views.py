from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Shelter
from .models import User
from .models import Kriteria
# D3
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import tree
from django.conf import settings
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import os
from .models import Train
# main
# Index
def index(request):
    return render(request, 'index.html')

def home(request):
    shelters = Shelter.objects.all()
    return render(request, 'home.html', {'shelters': shelters})

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
        import matplotlib
        matplotlib.use('Agg')

        # Gunakan Data training dari model Train
        training_data = Train.objects.all()
        df = pd.DataFrame(list(training_data.values('atap', 'rangka_atap', 'kolom_bangunan', 'decision')))
        
        if df.empty:
            raise ValueError("No training data available")

        # ambil data dari tebel kriteria dimana nama kriterianya = ATAP
        # kriteria_atap = Kriteria.objects.filter(nama_kriteria='ATAP')
        # kriteria_rangka_atap = Kriteria.objects.filter(nama_kriteria='RANGKA ATAP')
        # kriteria_kolom_bangunan = Kriteria.objects.filter(nama_kriteria='KOLOM BANGUNAN')
        # Map categorical values to numeric values
        atap_mapping = {'Seng': 1, 'Asbes': 2, 'Genteng': 3, 'Cor': 4}
        rangka_atap_mapping = {'Kayu': 1, 'Baja ringan': 1, 'Besi': 2, 'Beton': 3}
        kolom_bangunan_mapping = {'Kayu': 1, 'Baja ringan': 1, 'Besi': 2, 'Beton berulang': 3}
        decision_mapping = {'Secure': 1, 'Un-Secure': 0}

        # Mapping for training data
        df['atap'] = df['atap'].map(atap_mapping).fillna(0)
        df['rangka_atap'] = df['rangka_atap'].map(rangka_atap_mapping).fillna(0)
        df['kolom_bangunan'] = df['kolom_bangunan'].map(kolom_bangunan_mapping).fillna(0)
        df['decision'] = df['decision'].map(decision_mapping)

        # Define features and target for training
        features = ['atap', 'rangka_atap', 'kolom_bangunan']
        xTrain = df[features]
        yTrain = df['decision']

        # Train Decision Tree model
        dtree = DecisionTreeClassifier()
        dtree.fit(xTrain, yTrain)

        # Visualize Decision Tree
        plt.figure(figsize=(20, 20), facecolor='none')  # Set facecolor to 'none'
        plot_tree(dtree, feature_names=features, class_names=['Un-Secure', 'Secure'], filled=True)
        
        # Save plot to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)  # Set transparent to True
        buf.seek(0)
        plt.close()

        # Encode the plot to base64
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

        if request.method == 'POST':
            # Retrieve data from the form
            atap = request.POST.get('atap', '')
            rangka_atap = request.POST.get('rangka_atap', '')
            kolom_bangunan = request.POST.get('kolom_bangunan', '')
            latitude_longitude = request.POST.get('latitude_longitude', '')

            # Map form values to numeric values
            atap_value = atap_mapping.get(atap.capitalize(), 0)
            rangka_atap_value = rangka_atap_mapping.get(rangka_atap.replace('_', ' ').capitalize(), 0)
            kolom_bangunan_value = kolom_bangunan_mapping.get(kolom_bangunan.replace('_', ' ').capitalize(), 0)

            # Create DataFrame for testing data
            test_data = pd.DataFrame({
                'atap': [atap_value],
                'rangka_atap': [rangka_atap_value],
                'kolom_bangunan': [kolom_bangunan_value]
            })
            print(test_data)
            # Predict
            hasilPrediksi = dtree.predict(test_data)
            hasilPrediksi_label = 'Secure' if hasilPrediksi[0] == [1] else 'Un-Secure'
            print(hasilPrediksi)
            print(hasilPrediksi_label)
            # Prepare context
            context = {
                'image_base64': image_base64,
                'prediction': hasilPrediksi_label,
                'testing_data': test_data.to_html(),
                'latitude_longitude': latitude_longitude,
                'shelters': Shelter.objects.all()
            }
            messages.success(request, f": {hasilPrediksi_label}")
            return render(request, 'home.html', context)

        return HttpResponse("Invalid request method", status=400)

    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"An error occurred: {str(e)}")
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

def laporan(request):
    shelters = Shelter.objects.all()
    return render(request, 'pages/laporan.html', {'shelters': shelters})
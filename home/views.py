from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Shelter
from .models import User
from .models import Kriteria
from .models import Classification
import random
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
from sklearn.model_selection import cross_val_score, KFold
from graphviz import Digraph

# main
# Index
def index(request):
    return render(request, 'index.html')

def home(request):
    shelters = Classification.objects.all()
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
        return redirect('/shelter')  

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
        if request.method == 'POST':
            latitude_longitude = request.POST.get('latitude_longitude', '')
            # reverse
            # latitude_longitude = latitude_longitude.split(',')
            # latitude_longitude = latitude_longitude[::-1]
            # latitude_longitude = ','.join(latitude_longitude)
            # remove ['latitute', 'longitude']
            latitude_longitude = latitude_longitude.replace('latitude', '')
            latitude_longitude = latitude_longitude.replace('longitude', '')
            latitude_longitude = latitude_longitude.replace('(', '')
            latitude_longitude = latitude_longitude.replace(')', '')
            latitude_longitude = latitude_longitude.replace(':', '')
            latitude_longitude = latitude_longitude.replace(' ', '')
                    
            
            print(latitude_longitude)
            cekData = Classification.objects.filter(latitude_longitude=latitude_longitude).exists()
            
            if cekData:
                messages.success(request, "Aman.")
            else:
                messages.error(request, "Tidak Aman.")
                
            context = {
                'latitude_longitude': latitude_longitude,
                'shelters': Shelter.objects.all()
            }
            return render(request, 'home.html', context)

        return HttpResponse("Invalid request method", status=400)

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

def laporan(request):
    shelters = Classification.objects.all()
    return render(request, 'pages/laporan.html', {'shelters': shelters})


# Graph
def create_decision_tree_graph():
    dot = Digraph(comment='Pohon Keputusan Keamanan Bangunan')

    # Menambahkan node untuk setiap keputusan
    dot.node('Kolom Bangunan', 'Kolom Bangunan')
    dot.node('Kayu', 'Kayu')    
    dot.node('Baja Ringan', 'Baja Ringan')
    dot.node('Besi', 'Besi')
    dot.node('Beton Berulang', 'Beton Berulang')
    dot.node('Rangka Atap', 'Rangka Atap')
    dot.node('Kayu_Rangka', 'Kayu')
    dot.node('Baja Ringan_Rangka', 'Baja Ringan')
    dot.node('Besi_Rangka', 'Besi')
    dot.node('Atap', 'Atap')
    dot.node('Seng', 'Seng')
    dot.node('Asbes', 'Asbes')
    dot.node('Cor', 'Cor')
    dot.node('Un-Secure', 'Un-Secure')
    dot.node('Secure', 'Secure')

    # Menambahkan edges sesuai dengan aturan
    dot.edge('Kolom Bangunan', 'Kayu', label='[Kayu = 1.0]')
    dot.edge('Kolom Bangunan', 'Baja Ringan', label='[Baja Ringan = 1.0]')
    dot.edge('Kolom Bangunan', 'Besi', label='[Besi = 2.0]')
    dot.edge('Kolom Bangunan', 'Beton Berulang', label='[Beton Berulang = 3.0]')
    dot.edge('Kayu', 'Un-Secure')
    dot.edge('Baja Ringan', 'Un-Secure')
    dot.edge('Besi', 'Rangka Atap')
    dot.edge('Beton Berulang', 'Secure')
    dot.edge('Rangka Atap', 'Kayu_Rangka', label='[Kayu = 1.0]')
    dot.edge('Rangka Atap', 'Baja Ringan_Rangka', label='[Baja Ringan = 1.0]')
    dot.edge('Rangka Atap', 'Besi_Rangka', label='[Besi = 2.0]')
    dot.edge('Kayu_Rangka', 'Un-Secure')
    dot.edge('Baja Ringan_Rangka', 'Atap')
    dot.edge('Besi_Rangka', 'Secure')
    dot.edge('Atap', 'Seng', label='[Seng = 1.0]')
    dot.edge('Atap', 'Asbes', label='[Asbes = 2.0]')
    dot.edge('Atap', 'Cor', label='[Cor = 3.0]')
    dot.edge('Seng', 'Un-Secure')
    dot.edge('Asbes', 'Un-Secure')
    dot.edge('Cor', 'Secure')

    return dot

def decision_tree(request):
    import matplotlib
    matplotlib.use('Agg')

    # Ambil data pelatihan dari model Train
    training_data = Train.objects.all()
    df = pd.DataFrame(list(training_data.values('atap', 'rangka_atap', 'kolom_bangunan', 'decision')))
    
    if df.empty:
        raise ValueError("No training data available")

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
    dtree = DecisionTreeClassifier(criterion='entropy')
    dtree.fit(xTrain, yTrain)

    # Visualize Decision Tree using graphviz
    dot = create_decision_tree_graph()
    dot.render('pohon_keputusan_aturan', format='png', cleanup=True)

    # Encode the image to base64
    with open('pohon_keputusan_aturan.png', 'rb') as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

    # Get feature importances
    importances = dtree.feature_importances_
    feature_importances = {feature: importance for feature, importance in zip(features, importances)}

    # Retrieve data from Shelter model
    shelters = Shelter.objects.all()
    if shelters.count() == 0:
        raise ValueError("No shelter data available")

    # Prepare data for prediction
    shelter_data = []
    for shelter in shelters:
        atap_value = float(atap_mapping.get(shelter.atap, 0))
        rangka_atap_value = float(rangka_atap_mapping.get(shelter.rangka_atap, 0))
        kolom_bangunan_value = float(kolom_bangunan_mapping.get(shelter.kolom_bangunan, 0))
       
        shelter_data.append({
            'id': shelter.id,
            'latitude_longiitude': shelter.latitude_longitude,
            'atap': atap_value,
            'rangka_atap': rangka_atap_value,
            'kolom_bangunan': kolom_bangunan_value,
            'alamat': shelter.alamat
        })

    # Create DataFrame for shelter data
    test_data_df = pd.DataFrame([{
        'atap': shelter['atap'],
        'rangka_atap': shelter['rangka_atap'],
        'kolom_bangunan': shelter['kolom_bangunan']
    } for shelter in shelter_data])

    # Predict
    predictions = dtree.predict(test_data_df)
    predictions_labels = ['Secure' if pred == 1 else 'Un-Secure' for pred in predictions]

    # Attach predictions to shelter data    
    for i, shelter in enumerate(shelter_data):
        shelter['prediction'] = predictions_labels[i]

    # Prepare context
    context = {
        'image_base64': image_base64,
        'shelters': shelter_data,
        'feature_importances': feature_importances
    }

    return render(request, 'pages/dtree.html', context)



# Save Classification
def save_classification(request):
    if request.method == 'POST':
        latitude_longitude = request.POST.getlist('kordinat')
        atap = request.POST.getlist('atap')
        rangka_atap = request.POST.getlist('rangka_atap')
        kolom_bangunan = request.POST.getlist('kolom_bangunan')
        prediction = request.POST.getlist('prediction')
        alamat = request.POST.getlist('alamat')

        for i in range(len(latitude_longitude)):
            if Classification.objects.filter(latitude_longitude=latitude_longitude[i]).exists():
                continue

            Classification.objects.create(
                latitude_longitude=latitude_longitude[i],
                atap=atap[i],
                rangka_atap=rangka_atap[i],
                kolom_bangunan=kolom_bangunan[i],
                decision=prediction[i],
                alamat=alamat[i]
            )
        messages.success(request, "Data berhasil disimpan.")
        return redirect('/dashboard')

    return render(request, 'pages/dtree.html')

   
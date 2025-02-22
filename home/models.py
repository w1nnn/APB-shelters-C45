from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255) 
    nama = models.CharField(max_length=50)
    level = models.CharField(max_length=10)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Shelter(models.Model):
    id = models.AutoField(primary_key=True)
    nama_bangunan = models.CharField(max_length=255)
    latitude_longitude = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    atap = models.CharField(max_length=50, default='default_atap')
    rangka_atap = models.CharField(max_length=50, default='default_rangka_atap')
    kolom_bangunan = models.CharField(max_length=50, default='default_kolom_bangunan')
    status = models.CharField(max_length=50, default='default_status')
    
    def __str__(self):
        return self.nama_bangunan

    class Meta:
        verbose_name = "Shelter"
        verbose_name_plural = "Shelters"

class Kriteria(models.Model):
    id = models.AutoField(primary_key=True)
    nama_kriteria = models.CharField(max_length=50, default='Default Kriteria')
    sub_kriteria = models.CharField(max_length=50, default='Default Sub Kriteria')
    bobot = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.nama_kriteria} - {self.sub_kriteria}'

    class Meta:
        verbose_name = "Kriteria"
        verbose_name_plural = "Kriteria"

# Tabel Train isinya aatap, rangka_atap, kolom_bangunan, status
class Train(models.Model):
    id = models.AutoField(primary_key=True)
    atap = models.CharField(max_length=50)
    rangka_atap = models.CharField(max_length=50)
    kolom_bangunan = models.CharField(max_length=50)
    decision = models.CharField(max_length=50)

    def __str__(self):
        return self.decision

    class Meta:
        verbose_name = "Train"
        verbose_name_plural = "Trains"

class Classification(models.Model):
    id = models.AutoField(primary_key=True)
    latitude_longitude = models.CharField(max_length=255)
    atap = models.CharField(max_length=50)
    rangka_atap = models.CharField(max_length=50)
    kolom_bangunan = models.CharField(max_length=50)
    decision = models.CharField(max_length=50)
    alamat = models.CharField(max_length=255)

    def __str__(self):
        return self.decision

    class Meta:
        verbose_name = "Classification"
        verbose_name_plural = "Classifications"
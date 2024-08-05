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

    def __str__(self):
        return self.nama_bangunan

    class Meta:
        verbose_name = "Shelter"
        verbose_name_plural = "Shelters"

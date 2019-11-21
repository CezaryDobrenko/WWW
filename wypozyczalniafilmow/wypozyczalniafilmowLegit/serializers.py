from rest_framework import serializers
from .models import *

class RezyserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezyser
        fields = ['id', 'Imie', 'Nazwisko']

class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['id', 'Imie', 'Nazwisko', 'PESEL', 'Ulica', 'Miasto', 'Telefon']

class PlatnosciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platnosci
        fields = ['id', 'Zaliczka', 'Doplata']

class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = ['id', 'Imie', 'Nazwisko', 'PESEL', 'Stanowisko', 'Wiek']

class GatunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatunek
        fields = ['id', 'Gatunek']

class FilmySerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmy
        fields = ['id', 'rezyser', 'gatunek', 'Tytul_PL', 'Tytul_ENG', 'Rok_premiery','Czas_trwania']

class Rejestr_wypozyczenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rejestr_wypozyczen
        fields = ['id', 'filmy', 'platnosci', 'pracownik', 'klient', 'Data_wypozyczenia','Data_zwrotu']
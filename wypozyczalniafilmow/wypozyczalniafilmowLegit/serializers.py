from rest_framework import serializers

class RezyserSerializer(serializers.Serializer):
    Imie = serializers.CharField(max_length=45)
    Nazwisko = serializers.CharField(max_length=45)

class KlientSerializer(serializers.Serializer):
    Imie = serializers.CharField(max_length=45)
    Nazwisko = serializers.CharField(max_length=45)
    PESEL = serializers.CharField(max_length=11)
    Ulica = serializers.CharField(max_length=45)
    Misasto = serializers.CharField(max_length=45)
    Telefon = serializers.CharField(max_length=15)

class PlatnosciSerializer(serializers.Serializer):
    Zaliczka = serializers.CharField(max_length=45)
    Doplata = serializers.CharField(max_length=45)

class PracownikSerializer(serializers.Serializer):
    Imie = serializers.CharField(max_length=45)
    Nazwisko = serializers.CharField(max_length=45)
    PESEL = serializers.CharField(max_length=11)
    Stanowisko = (
        ('JR', 'Junior'),
        ('MID', 'Mid'),
        ('SR', 'Senior'),
    )
    Wiek = serializers.CharField(max_length=2)

class GatunekSerializer(serializers.Serializer):
    Zaliczka = serializers.CharField(max_length=45)
    Doplata = serializers.CharField(max_length=45)


class FilmySerializer(serializers.Serializer):
    Tytul_PL = serializers.CharField(max_length=45)
    Tytul_ENG = serializers.CharField(max_length=45)
    Rok_premiery = serializers.DateTimeField('data publikacji')
    Czas_trwania = serializers.CharField(max_length=45)

class Rejestr_wypozyczenSerializer(serializers.Serializer):
    Data_wypozyczenia = serializers.DateTimeField('data wypozyczenia')
    Data_zwrotu = serializers.DateTimeField('data zwrotu')
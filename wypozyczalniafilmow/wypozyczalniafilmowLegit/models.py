from django.db import models

class Rezyser(models.Model):
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)

class Klient(models.Model):
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    PESEL = models.CharField(max_length=11)
    Ulica = models.CharField(max_length=45)
    Misasto = models.CharField(max_length=45)
    Telefon = models.CharField(max_length=15)

class Platnosci(models.Model):
    Zaliczka = models.CharField(max_length=45)
    Doplata = models.CharField(max_length=45)

class Pracownik(models.Model):
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    PESEL = models.CharField(max_length=11)
    Stanowisko = (
        ('JR', 'Junior'),
        ('MID', 'Mid'),
        ('SR', 'Senior'),
    )
    PESEL = models.CharField(max_length=2)

class Gatunek(models.Model):
    Zaliczka = models.CharField(max_length=45)
    Doplata = models.CharField(max_length=45)

class Filmy(models.Model):
    rezyser = models.ForeignKey(Rezyser, on_delete=models.CASCADE)
    gatunek = models.ForeignKey(Gatunek, on_delete=models.CASCADE)
    Tytul_PL = models.CharField(max_length=45)
    Tytul_ENG = models.CharField(max_length=45)
    Rok_premiery = models.DateTimeField('data publikacji')
    Czas_trwania = models.CharField(max_length=45)

class Rejestr_wypozyczen(models.Model):
    filmy = models.ForeignKey(Filmy, on_delete=models.RESTRICT )
    platnosci = models.ForeignKey(Platnosci, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.RESTRICT)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    Data_wypozyczenia = models.DateTimeField('data wypozyczenia')
    Data_zwrotu = models.DateTimeField('data zwrotu')
from django.http import HttpResponse
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from django.http import JsonResponse
from rest_framework.response import Response

@api_view(['GET','POST'])
def Klient_list(request):
    if request.method == 'GET':
        Klienci = Klient.objects.all()
        serializer = KlientSerializer(Klienci, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = KlientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Klient_detail(request, pk):
    try:
        klient = Klient.objects.get(pk=pk)
    except Klient.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = KlientSerializer(klient)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = KlientSerializer(klient, request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        klient.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def Pracownik_list(request):
    if request.method == 'GET':
        Pracownicy = Pracownik.objects.all()
        serializer = PracownikSerializer(Pracownicy, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PracownikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Pracownik_detail(request, pk):
    try:
        pracownik = Pracownik.objects.get(pk=pk)
    except Pracownik.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = PracownikSerializer(pracownik)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = PracownikSerializer(pracownik, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        pracownik.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def Rezyser_list(request):
    if request.method == 'GET':
        Rerzyserzy = Rezyser.objects.all()
        serializer = RezyserSerializer(Rerzyserzy, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = RezyserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Rezyser_detail(request, pk):
    try:
        rezyser = Rezyser.objects.get(pk=pk)
    except Rezyser.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = RezyserSerializer(rezyser)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = RezyserSerializer(rezyser, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        rezyser.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def Film_list(request):
    if request.method == 'GET':
        Film = Filmy.objects.all()
        serializer = FilmySerializer(Film, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = FilmySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Film_detail(request, pk):
    try:
        Film = Filmy.objects.get(pk=pk)
    except Rezyser.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = FilmySerializer(Film)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = FilmySerializer(Film, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        Film.delete()
        return Response(status.HTTP_204_NO_CONTENT)
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
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = PracownikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Pracownik_detail(request, pk):
    try:
        pracownik = Pracownik.objects.get(pk=pk)
    except Pracownik.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = PracownikSerializer(pracownik)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        serializer = PracownikSerializer(pracownik, request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        pracownik.delete()
        return Response(status.HTTP_204_NO_CONTENT)
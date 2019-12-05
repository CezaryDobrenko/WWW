from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from django.http import Http404

class Klient_list(APIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

   def get(self, request, format=None):
       Klienci = Klient.objects.all()
       serializer = KlientSerializer(Klienci, many=True)
       return Response(serializer.data)

   def post(self, request, format=None):
       serializer = KlientSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save(owner=self.request.user)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Klient_detail(APIView):
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

   def get_object(self, pk):
       try:
           return Klient.objects.get(pk=pk)
       except Klient.DoesNotExist:
           raise Http404

   def get(self, request, pk, format=None):
       question = self.get_object(pk)
       serializer = KlientSerializer(question)
       return Response(serializer.data)

   def put(self, request, pk, format=None):
       question = self.get_object(pk)
       serializer = KlientSerializer(question, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, pk, format=None):
       question = self.get_object(pk)
       question.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



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
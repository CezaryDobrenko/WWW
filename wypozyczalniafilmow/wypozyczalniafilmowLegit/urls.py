from django.urls import path
from . import views

urlpatterns = [
    path('klienci', views.Klient_list),
    path('klient/<int:pk>', views.Klient_detail),
    path('pracownicy', views.Pracownik_list),
    path('pracownik/<int:pk>', views.Pracownik_detail),
    path('rezyserzy', views.Rezyser_list),
    path('rezyser/<int:pk>', views.Rezyser_detail),
    path('filmy', views.Film_list),
    path('film/<int:pk>', views.Film_detail),
]

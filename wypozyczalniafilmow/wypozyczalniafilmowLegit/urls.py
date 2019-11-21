from django.urls import path
from . import views

urlpatterns = [
    path('klienci', views.Klient_list),
    path('klienci/<int:pk>', views.Klient_detail),
    path('pracownicy', views.Pracownik_list),
    path('pracownicy/<int:pk>', views.Pracownik_detail)
]

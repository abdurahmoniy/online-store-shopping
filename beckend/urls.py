from .views import *
from django.urls import path

urlpatterns = [
    path("", home),
    path('index/', index, name='Bosh sahifa'),
    path('contact/', contact, name='contact'),
    path('kiyimlar/', kiyimlar, name='kiyimlar'),
]
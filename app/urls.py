from django.urls import path
from app.views import *
app_name='anything'

urlpatterns = [
    path('firstFbv/', firstFbv, name = 'firstFbv'),
    path('secondFbv/', secondFbv, name='secondFbv'),
    path('xyz/', xyz, name = 'xyz'),
]
from django.urls import path
from . import views

urlpatterns = [
    #URL pour telephone
    path('', views.main, name=('main')),
    #URL pour categorie
]

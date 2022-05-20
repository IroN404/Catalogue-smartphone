from django.urls import path
from . import views, categorie_views

urlpatterns = [
    #URL pour telephone
    path('', views.main, name=('main')),
    path('ajout/', views.ajout, name=('ajout')),
    path('traitement/', views.traitement, name=('traitement')),
    #URL pour categorie
    path('ajoutcategorie/', categorie_views.ajout, name=('ajout')),
    path('traitementcategorie/', categorie_views.traitement, name=('traitement')),
]

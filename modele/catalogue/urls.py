from django.urls import path
from . import views, categorie_views

urlpatterns = [
    #URL pour telephone
    path('', views.main, name=('main')),
    path('ajout/', views.ajout, name=('ajout')),
    path('traitement/', views.traitement, name=('traitement')),
    path('infos/', views.infos, name=('infos')),
    path('affiche/<int:id>/', views.affiche, name=('affiche')),
    path('update/<int:id>/', views.update, name=('update')),
    path('updatetraitement/<int:id>/', views.updatetraitement, name=('updatetraitement')),
    #URL pour categorie
    path('ajoutcategorie/', categorie_views.ajout, name=('ajout')),
    path('traitementcategorie/', categorie_views.traitement, name=('traitement')),
    path('infoscategorie/', categorie_views.infos, name=('infos')),
    path('infoscategorie/', categorie_views.infos, name=('infos')),
    path('affichecategorie/<int:id>/', categorie_views.affiche, name=('affiche')),
    path('updatecategorie/<int:id>/', categorie_views.update, name=('update')),
    path('updatetraitementcategorie/<int:id>/', categorie_views.updatetraitement, name=('updatetraitement')),
]

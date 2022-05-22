from django.urls import path
from . import views, categorie_views

urlpatterns = [
    #URL pour telephone
    path('', views.main, name=('main')),
    path('ajout/<int:id>/', views.ajout, name=('ajout')),
    path('traitement/<int:id>/', views.traitement, name=('traitement')),
    path('infos/', views.infos, name=('infos')),
    path('affiche/<int:id>/', views.affiche, name=('affiche')),
    path('update/<int:id>/', views.update, name=('update')),
    path('updatetraitement/<int:id>/', views.updatetraitement, name=('updatetraitement')),
    path('delete/<int:id>/', views.delete, name=('delete')),
    #URL pour categorie
    path('ajoutcategorie/', categorie_views.ajout, name=('ajout')),
    path('traitementcategorie/', categorie_views.traitement, name=('traitement')),
    path('infoscategorie/', categorie_views.infos, name=('infos')),
    path('affichecategorie/<int:id>/', categorie_views.affiche, name=('affichecategorie')),
    path('updatecategorie/<int:id>/', categorie_views.update, name=('update')),
    path('updatetraitementcategorie/<int:id>/', categorie_views.updatetraitement, name=('updatetraitement')),
    path('deletecategorie/<int:id>/', categorie_views.delete, name=('delete')),
]
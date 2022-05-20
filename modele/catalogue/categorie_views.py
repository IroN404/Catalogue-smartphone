from django.shortcuts import render
from .forms import CategorieForm
# Create your views here.

def ajout(request):
    if request.method == 'POST':
        form = CategorieForm(request)
        return render(request,"categorie/ajout.html", {"form":form})
    else:
        form = CategorieForm()
        return render(request, "categorie/ajout.html", {"form": form})

def traitement(request):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save()
        return render(request,"categorie/traitement.html", {"categorie" : categorie})
    else :
        return render(request,"categorie/ajout.html",{"form": cform})
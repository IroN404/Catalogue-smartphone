from django.shortcuts import render, HttpResponseRedirect
from .forms import CategorieForm
from . import models
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
        return HttpResponseRedirect("/infoscategorie")
    else :
        return render(request,"categorie/ajout.html",{"form": cform})

def infos(request):
    liste = list(models.Categorie.objects.all())
    return render(request,"categorie/infos.html", {"liste" : liste})

def affiche(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    liste = models.Telephone.objects.filter(categorie_id = id)
    return render(request, "categorie/affiche.html", {"categorie":categorie, "liste" : liste})

def update(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    form = CategorieForm(categorie.dico())
    return render(request, "categorie/update.html",{"form":form, "id":id})

def updatetraitement(request, id):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save(commit=False)
        categorie.id = id
        categorie.save()
        return HttpResponseRedirect("/infoscategorie")
    else:
        return render(request, "categorie/update.html", {"form": cform, "id":id})

def delete(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    telephone = models.Telephone.objects.filter(categorie_id = id)
    categorie.delete()
    telephone.delete()
    return HttpResponseRedirect("/infoscategorie/")

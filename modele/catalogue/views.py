from django.shortcuts import render, HttpResponseRedirect
from .forms import TelephoneForm
from . import models
# Create your views here.

def main(request):
    return render(request,"telephone/main.html")

def ajout(request, id):
    if request.method == 'POST':
        form = TelephoneForm(request)
        return render(request,"telephone/ajout.html", {"form":form, "id":id})
    else:
        form = TelephoneForm()
        return render(request, "telephone/ajout.html", {"form": form, "id":id})

def traitement(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    tform = TelephoneForm(request.POST)
    if tform.is_valid():
        telephone = tform.save(commit=False)
        telephone.categorie = categorie
        telephone.categorie_id = id
        telephone.save()
        return HttpResponseRedirect("/infos")
    else :
        return render(request,"telephone/ajout.html", {"form": tform})

def infos(request):
    liste = list(models.Telephone.objects.all())
    return render(request, "telephone/infos.html",{"liste" : liste})

def affiche(request, id):
    telephone = models.Telephone.objects.get(pk=id)
    return render(request, "telephone/affiche.html", {"telephone":telephone})

def update(request, id):
    telephone = models.Telephone.objects.get(pk=id)
    form = TelephoneForm(telephone.dico())
    return render(request, "telephone/update.html",{"form":form, "id":id})

def updatetraitement(request, id):
    tform = TelephoneForm(request.POST)
    if tform.is_valid():
        telephone = tform.save(commit=False)
        telephone.id = id
        telephone.save()
        return HttpResponseRedirect("/infos")
    else:
        return render(request, "telephone/update.html", {"form": tform, "id":id})

def delete(request, id):
    telephone = models.Telephone.objects.get(pk=id)
    telephone.delete()
    return HttpResponseRedirect("/infos/")
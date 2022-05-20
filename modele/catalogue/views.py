from django.shortcuts import render, HttpResponseRedirect
from .forms import TelephoneForm
from . import models
# Create your views here.

def main(request):
    return render(request,"telephone/main.html")

def ajout(request):
    if request.method == 'POST':
        form = TelephoneForm(request)
        return render(request,"telephone/ajout.html", {"form":form})
    else:
        form = TelephoneForm()
        return render(request, "telephone/ajout.html", {"form": form})

def traitement(request):
    tform = TelephoneForm(request.POST)
    if tform.is_valid():
        telephone = tform.save()
        return HttpResponseRedirect("/infos")
    else :
        return render(request,"telephone/ajout.html", {"form": tform})

def infos(request):
    liste = list(models.Telephone.objects.all())
    return render(request, "telephone/infos.html",{"liste" : liste})

def affiche(request, id):
    telephone = models.Telephone.objects.get(pk=id)
    return render(request, "telephone/affiche.html", {"telephone":telephone})
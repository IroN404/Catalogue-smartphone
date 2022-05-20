from django.shortcuts import render
from .forms import TelephoneForm
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
        return render(request,"telephone/traitement.html", {"telephone" : telephone})
    else :
        return render(request,"telephone/ajout.html", {"form": tform})
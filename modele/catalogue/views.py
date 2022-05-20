from django.shortcuts import render
from .forms import TelephoneForm
# Create your views here.

def ajout(request):
    if request.method == 'POST':
        form = TelephoneForm(request)
        return render(request,"/ajout.html", {"form":form})
    else:
        form = TelephoneForm()
        return render(request, "/ajout.html", {"form": form})
from django.shortcuts import render, HttpResponseRedirect
from .forms import EnseignantForm
from . import models

# Create your views here.

def saisieeng(request):
        cform = EnseignantForm()
        return render(request, "enseignant/saisie.html", {"form":cform})

def traitementeng(request):
    cform = EnseignantForm(request.POST, request.FILES)
    if cform.is_valid():
        enseignant = cform.save()
        return HttpResponseRedirect('/absence/enseignant')
    else:
        return render(request, "enseignant/saisie.html", {"form":cform})

def enseignant(request):
    liste = list(models.Enseignant.objects.all())
    return render(request,"enseignant/accueil.html", {"liste":liste})

def affichageeng(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    return render(request, "enseignant/affiche.html", {"enseignant":enseignant})

def updateeng(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    form = EnseignantForm(enseignant.dico())
    return render(request, "enseignant/saisie.html", {"form":form, "id":id})

def updatetraitementeng (request, id):
    cform = EnseignantForm(request.POST, request.FILES)
    if cform.is_valid():
        enseignant = cform.save(commit=False)
        enseignant.id = id
        enseignant.save()
        return HttpResponseRedirect("/absence/enseignant")
    else:
        return render(request, "enseignant/saisie.html", {"form": cform, "id":id})

def deleteeng (request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    enseignant.delete()
    return HttpResponseRedirect("/absence/enseignant")
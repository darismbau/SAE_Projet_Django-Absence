from django.shortcuts import render, HttpResponseRedirect
from .forms import EtudiantForm
from . import models
from .models import Etudiant

# Create your views here.

def saisieetu(request):
        cform = EtudiantForm(request.POST, request.FILES)
        return render(request, "etudiant/saisie.html", {"form":cform})

def traitementetu(request):
    cform = EtudiantForm(request.POST, request.FILES)
    if cform.is_valid():
        etudiant = cform.save()
        return HttpResponseRedirect('/absence/etudiant')
    else:
        return render(request, "etudiant/saisie.html", {"form":cform})

def etudiant(request):
    liste = list(models.Etudiant.objects.all())
    return render(request,"etudiant/accueil.html", {"liste":liste, 'data':Etudiant.objects.all()})

def affichageetu(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    return render(request, "etudiant/affiche.html", {"etudiant":etudiant, 'data':Etudiant.objects.all()})

def updateetu(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    form = EtudiantForm(etudiant.dico())
    return render(request, "etudiant/saisie.html", {"form":form, "id":id})

def updatetraitementetu (request, id):
    cform = EtudiantForm(request.POST, request.FILES)
    if cform.is_valid():
        etudiant = cform.save(commit=False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("/absence/etudiant")
    else:
        return render(request, "etudiant/saisie.html", {"form": cform, "id":id})

def deleteetu (request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/absence/etudiant")
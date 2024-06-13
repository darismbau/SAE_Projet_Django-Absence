from django.shortcuts import render, HttpResponseRedirect
from .forms import CoursForm
from . import models

# Create your views here.

def saisiecours(request):
        cform = CoursForm()
        return render(request, "cours/saisie.html", {"form":cform})

def traitementcours(request):
    cform = CoursForm(request.POST, request.FILES)
    if cform.is_valid():
        cours = cform.save()
        return HttpResponseRedirect('/absence/cours')
    else:
        return render(request, "cours/saisie.html", {"form":cform})

def cours(request):
    liste = list(models.Cours.objects.all())
    return render(request,"cours/accueil.html", {"liste":liste})

def affichagecours(request, id):
    cours = models.Cours.objects.get(pk=id)
    return render(request, "cours/affiche.html", {"cours":cours})

def updatecours(request, id):
    cours = models.Cours.objects.get(pk=id)
    form = CoursForm(cours.dico())
    return render(request, "cours/saisie.html", {"form":form, "id":id})

def updatetraitementcours (request, id):
    cform = CoursForm(request.POST)
    if cform.is_valid():
        cours = cform.save(commit=False)
        cours.id = id
        cours.save()
        return HttpResponseRedirect("/absence/cours")
    else:
        return render(request, "cours/saisie.html", {"form": cform, "id":id})

def deletecours (request, id):
    cours = models.Cours.objects.get(pk=id)
    cours.delete()
    return HttpResponseRedirect("/absence/cours")
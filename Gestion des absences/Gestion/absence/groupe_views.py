from django.shortcuts import render, HttpResponseRedirect
from .forms import GroupeForm
from . import models

# Create your views here.

def saisiegr(request):
        cform = GroupeForm()
        return render(request, "groupe/saisie.html", {"form":cform})

def traitementgr(request):
    cform = GroupeForm(request.POST)
    if cform.is_valid():
        groupe = cform.save()
        return HttpResponseRedirect('/absence/groupe')
    else:
        return render(request, "groupe/saisie.html", {"form":cform})

def groupe(request):
    liste = list(models.Groupe.objects.all())
    return render(request,"groupe/accueil.html", {"liste":liste})

def affichagegr(request, id):
    groupe = models.Groupe.objects.get(pk=id)
    return render(request, "groupe/affiche.html", {"groupe":groupe})

def updategr(request, id):
    groupe = models.Groupe.objects.get(pk=id)
    form = GroupeForm(groupe.dico())
    return render(request, "groupe/saisie.html", {"form":form, "id":id, "groupe":groupe})

def updatetraitementgr (request, id):
    cform = GroupeForm(request.POST)
    if cform.is_valid():
        groupe = cform.save(commit=False)
        groupe.id = id
        groupe.save()
        return HttpResponseRedirect("/absence/groupe")
    else:
        return render(request, "groupe/saisie.html", {"form": cform, "id":id, "groupe":groupe})

def deletegr (request, id):
    groupe = models.Groupe.objects.get(pk=id)
    groupe.delete()
    return HttpResponseRedirect("/absence/groupe")
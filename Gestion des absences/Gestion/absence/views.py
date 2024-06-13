from django.shortcuts import render, HttpResponseRedirect , get_object_or_404
from .forms import AbsenceForm
from . import forms
from . import models
import xhtml2pdf.pisa as pisa
from io import BytesIO
from django.template.loader import get_template
from .models import Etudiant, Absence

# Create your views here.

def absence(request):
    liste = list(models.Absence.objects.all())
    return render(request,"absence/accueil.html",{"liste":liste})
def saisie(request):
    if request.method == "POST":
        form = AbsenceForm(request)
        return render(request,"absence/saisie.html",{"form":form})
    else:
        form = AbsenceForm()
        return render(request, "absence/saisie.html" ,{"form":form})
def traitement(request):
    lform = AbsenceForm(request.POST, request.FILES)
    if lform.is_valid():
        absence = lform.save()
        return HttpResponseRedirect("/absence")
    else:
        return render(request,"absence/saisie.html",{"form":lform})
def affichage(resquest,id):
    absence = models.Absence.objects.get(pk=id)
    return render(resquest, "absence/affiche.html", {"absence":absence})

def update(request, id):
    absence = models.Absence.objects.get(pk=id)
    form = AbsenceForm(absence.dico())
    return render(request, "absence/saisie.html", {"form":form, "id":id})

def updatetraitement (request, id):
    lform = AbsenceForm(request.POST, request.FILES)
    if lform.is_valid():
        absence = lform.save(commit=False)
        absence.id = id
        absence.save()
        return HttpResponseRedirect("/absence")
    else:
        return render(request, "absence/saisie.html", {"form": lform, "id":id})

def delete (request, id):
    absence = models.Absence.objects.get(pk=id)
    absence.delete()
    return HttpResponseRedirect("/absence")



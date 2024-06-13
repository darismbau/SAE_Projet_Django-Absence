from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Groupe, Etudiant, Enseignant, Cours, Absence
from . import models

class AbsenceForm(ModelForm):
    class Meta:
        model = models.Absence
        fields = {'etudiant', 'cours' ,'justifie', 'justification',}
        labels = {
            'etudiant':_('Nom_étudiant'),
            'Cours':_('Cours'),
            'Justifie':_('Justifié'),
            'justification':_('Justification'),
        }

class GroupeForm(ModelForm):
    class Meta:
        model = models.Groupe
        fields = {'nom'}
        labels = {
            'nom':_('Nom du groupe'),
        }

class EnseignantForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = {'nom','prenom','email'}
        labels = {
            'nom':_('Nom'),
            'prenom':_('Prenom'),
            'email':_('Email'),
        }

class CoursForm(ModelForm):
    class Meta:
        model = models.Cours
        fields = {'titre_du_cours','date','duree','enseignant','groupe'}
        labels = {
            'titre_du_cours':_('Titre'),
            'date':_('Date'),
            'Duree':_('Durée'),
            'enseignant':_('Enseignant'),
            'groupe':_('Groupe'),
        }

class EtudiantForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = {'nom','prenom','email','photo','groupe'}
        labels = {
            'nom':_('Nom'),
            'prenom':_('Prénom'),
            'email':_('Email'),
            'photo':_('Photo'),
            'Groupe':_('Groupe'),
    }
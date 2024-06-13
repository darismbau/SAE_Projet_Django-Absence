from django.urls import path
from . import views , cours_views , enseignant_views , etudiant_views , groupe_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.absence),
    path('saisie/',views.saisie),
    path('traitement/',views.traitement),
    path('affichage/<int:id>/',views.affichage),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),
    #Cours
    path('cours/',cours_views.cours),
    path('saisiecours/', cours_views.saisiecours),
    path('traitementcours/', cours_views.traitementcours),
    path('affichagecours/<int:id>/', cours_views.affichagecours),
    path('updatecours/<int:id>/', cours_views.updatecours),
    path('updatetraitementcours/<int:id>/', cours_views.updatetraitementcours),
    path('deletecours/<int:id>/', cours_views.deletecours),
    #enseignant
    path('enseignant/',enseignant_views.enseignant),
    path('saisieeng/', enseignant_views.saisieeng),
    path('traitementeng/', enseignant_views.traitementeng),
    path('affichageeng/<int:id>/', enseignant_views.affichageeng),
    path('updateeng/<int:id>/', enseignant_views.updateeng),
    path('updatetraitementeng/<int:id>/', enseignant_views.updatetraitementeng),
    path('deleteeng/<int:id>/', enseignant_views.deleteeng),
    #etudiant
    path('etudiant/',etudiant_views.etudiant),
    path('saisieetu/', etudiant_views.saisieetu),
    path('traitementetu/', etudiant_views.traitementetu),
    path('affichageetu/<int:id>/', etudiant_views.affichageetu),
    path('updateetu/<int:id>/', etudiant_views.updateetu),
    path('updatetraitementetu/<int:id>/', etudiant_views.updatetraitementetu),
    path('deleteetu/<int:id>/', etudiant_views.deleteetu),
    #groupe
     path('groupe',groupe_views.groupe),
    path('saisiegr/', groupe_views.saisiegr),
    path('traitementgr/', groupe_views.traitementgr),
    path('affichagegr/<int:id>/', groupe_views.affichagegr),
    path('updategr/<int:id>/', groupe_views.updategr),
    path('updatetraitementgr/<int:id>/', groupe_views.updatetraitementgr),
    path('deletegr/<int:id>/', groupe_views.deletegr),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


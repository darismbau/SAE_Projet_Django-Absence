from django.db import models

# Create your models here.


class Groupe(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    def dico(self):
        return {"nom":self.nom}

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}, {self.email} du groupe : {self.groupe}"

    def dico(self):
        return {"nom":self.nom, "prenom":self.prenom, "email":self.email, "groupe":self.groupe, "photo":self.photo}

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.prenom} {self.nom}, {self.email}"

    def dico(self):
        return {"nom":self.nom, "prenom":self.prenom, "email":self.email}

class Cours(models.Model):
    titre_du_cours = models.CharField(max_length=200)
    date = models.DateField()
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    duree = models.DurationField()
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre_du_cours

    def dico(self):
        return {"titre_du_cours":self.titre_du_cours, "date":self.date, "enseignant":self.enseignant, "duree":self.duree, "groupe":self.groupe}

class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    justifie = models.BooleanField(default=False)
    justification = models.FileField(upload_to='photos',null=True, blank=True)

    def __str__(self):
        return f"{self.etudiant} - {self.cours}"

    def dico(self):
        return {"etudiant":self.etudiant, "cours":self.cours, "justifie":self.justifie, "justification":self.justification}






















































#class Groupes(models.Model):
#    id = models.AutoField(primary_key=True)
#    nom = models.CharField(max_length=100)

#class Etudiants(models.Model):
#     id = models.AutoField(primary_key=True)
#     nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     groupes_id = models.ForeignKey("Groupes", on_delete=models.CASCADE, default=None)
#class Enseignants(models.Model):
#     id = models.AutoField(primary_key=True)
#     nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)

#class Cours(models.Model):
#     id = models.AutoField(primary_key=True)
#     titre = models.CharField(max_length=100)
#     date = models.DateField(blank=True, null=True)
#     durée = models.DateTimeField(auto_now_add=True)
#     enseignants_id = models.ForeignKey("Enseignants", on_delete=models.CASCADE, default=None)
#     groupes_id = models.ForeignKey("Groupes", on_delete=models.CASCADE, default=None)

#class Absences(models.Model):
#     id=models.AutoField(primary_key=True)
#     justifie = models.BooleanField(default=False)
#     justification = models.FileField (upload_to='justificatifs')
#     etudiants_id = models.ForeignKey("Etudiants", on_delete=models.CASCADE, default=None)
#     cours_id = models.ForeignKey("Cours", on_delete=models.CASCADE, default=None)

#     def __str__(self):
#         chaine = f"{self.etudiants_id} ... models.Absent"
#         return chaine

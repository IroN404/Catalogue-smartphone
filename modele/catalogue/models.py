from django.db import models

# Create your models here.

class Telephone(models.Model):
    modele = models.CharField(max_length=100)
    stockage = models.IntegerField(blank=False)
    date_sortie = models.DateField(blank=False, null=True)
    details = models.TextField(blank=True, null=True)
    categorie = models.ForeignKey("categorie", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"Produit par {self.categorie}, le smartPhone {self.modele} possède {self.stockage} Go de stockage et est sortie le {self.date_sortie}."
        return chaine

    def dico(self):
        return {"modele": self.modele, "stockage": self.stockage, "date_sortie": self.date_sortie, "details": self.details, "categorie": self.categorie}

class Categorie(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom

    def dico(self):
        return {"nom":self.nom, "detail":self.details}
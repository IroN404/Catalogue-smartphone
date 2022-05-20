from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class TelephoneForm(ModelForm):
    class Meta:
        model = models.Telephone
        fields = ('modele','stockage','date_sortie','details')
        labels = {
            'modele' : _('Modèle'),
            'stockage' : _('Stockage'),
            'date_sortie' : _('Date de sortie'),
            'details' : _('Détails'),
        }

class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('nom', 'details')
        labels = {
            'nom' : _('Nom'),
            'details' : _('Détails'),
        }
from django.db import models
from django.contrib.auth.models import User


class Taches(models.Model):
    PRIORITE_CHOICES = [
        (1, 'Haute'),
        (2, 'Moyenne'),
        (3, 'Basse'),
    ]
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_echeance = models.DateTimeField()
    priorite = models.IntegerField(choices=PRIORITE_CHOICES)
    status = models.BooleanField(default=False)
    categorie = models.ForeignKey('Categorie',on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)
 
class Categorie(models.Model):
    type = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.type
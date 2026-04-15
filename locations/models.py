from django.db import models

class Location(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.TextField()

    def __str__(self):
        return self.nom
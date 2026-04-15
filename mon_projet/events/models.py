from django.db import models
from django.contrib.auth.models import User
from locations.models import Location

class Event(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    heure = models.TimeField()
    capacite_max = models.IntegerField()
    organisateur = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    lieu = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.titre
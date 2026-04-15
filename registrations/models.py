from django.db import models
from django.contrib.auth.models import User
from events.models import Event

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="pending")

    def __str__(self):
        return f"{self.user.username} -> {self.event.titre}"
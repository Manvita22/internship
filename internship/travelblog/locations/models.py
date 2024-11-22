from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null =True)  # Link to User
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/', blank=True, null=True)  # Renamed field for clarity

    def __str__(self):
        return self.name

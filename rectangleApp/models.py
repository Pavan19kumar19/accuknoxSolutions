from django.db import models

# Create your models here.
class Rectangular(models.Model):
    length = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Rectangular with length {self.length} and width {self.width}"

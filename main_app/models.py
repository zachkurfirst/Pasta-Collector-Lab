from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
class Pasta(models.Model):
    name = models.CharField(max_length=50)
    SMALL_PASTA = 'Small Pasta'
    RIBBON_CUT = 'Ribbon-Cut'
    TUBE_SHAPED = 'Tube-Shaped'
    STUFFED = 'Stuffed'
    TYPE_CHOICES = {
        SMALL_PASTA: 'Small Pasta',
        RIBBON_CUT: 'Ribbon-Cut',
        TUBE_SHAPED: 'Tube-Shaped',
        STUFFED: 'Stuffed',
    }
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default=SMALL_PASTA,
        )
    cook_time = models.IntegerField()

    def __str__(self):
        return self.name
    
    # handle redirect to detail page
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pasta_id': self.id})
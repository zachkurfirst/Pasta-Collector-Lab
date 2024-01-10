from django.db import models

# Create your models here.
class Pasta(models.Model):
    name = models.CharField(max_length=50)
    SMALL_PASTA = 'SM'
    RIBBON_CUT = 'RC'
    TUBE_SHAPED = 'TS'
    STUFFED = 'ST'
    TYPE_CHOICES = [
        (SMALL_PASTA, 'Small Pasta'),
        (RIBBON_CUT, 'Ribbon-Cut'),
        (TUBE_SHAPED, 'Tube-Shaped'),
        (STUFFED, 'Stuffed'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=SMALL_PASTA,
        )
    cook_time = models.DurationField()
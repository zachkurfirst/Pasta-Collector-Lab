from django.db import models
# Import the reverse function
from django.urls import reverse

PASTA_TYPES = (
    ('SM', 'Small Pasta'),
    ('RC', 'Ribbon-Cut'),
    ('TS', 'Tube-Shaped'),
    ('ST', 'Stuffed')
)

DIFFICULTY = (
    ('E', 'Easy'),
    ('M', 'Moderate'),
    ('D', 'Difficult')
)

# Create your models here.
class Pasta(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=2,
        choices=PASTA_TYPES,
        default=PASTA_TYPES[0][0],
        )
    cook_time = models.IntegerField()

    def __str__(self):
        return self.name
    
    # handle redirect to detail page
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pasta_id': self.id})
    
    # SMALL_PASTA = 'Small Pasta'
    # RIBBON_CUT = 'Ribbon-Cut'
    # TUBE_SHAPED = 'Tube-Shaped'
    # STUFFED = 'Stuffed'
    # TYPE_CHOICES = {
    #     SMALL_PASTA: 'Small Pasta',
    #     RIBBON_CUT: 'Ribbon-Cut',
    #     TUBE_SHAPED: 'Tube-Shaped',
    #     STUFFED: 'Stuffed',
    # }

class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    is_vegetarian = models.BooleanField()
    recipe_link = models.URLField()
    difficulty = models.CharField(
        'cook difficulty',
        max_length=1,
        choices=DIFFICULTY,
        default=DIFFICULTY[1][0]
        )
    # Create a pasta_id FK to satisfy 1:M relationship
    pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.get_difficulty_display()} difficulty"
    
    class Meta:
        ordering = ['difficulty']
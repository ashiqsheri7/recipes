from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    difficulty_level = models.CharField(max_length=50)
    preparation_time = models.IntegerField()  # in minutes
    vegetarian = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)

    def __str__(self):
        return self.name

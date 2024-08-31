from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True)  

    def __str__(self):
        return self.name

class Favorite(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe',)

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Rating out of 5

    def __str__(self):
        return f'Review for {self.recipe.name} - {self.rating}/5'
from rest_framework import serializers
from .models import Recipe, Favorite
from .models import Review

class RecipeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'ingredients', 'instructions', 'image', 'reviews']

class FavoriteSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)  # Use RecipeSerializer for GET requests
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(), write_only=True, source='recipe'
    )  # Accept only recipe_id for POST requests

    class Meta:
        model = Favorite
        fields = ['id', 'recipe', 'recipe_id', 'added_at']

    def create(self, validated_data):
        recipe = validated_data.get('recipe')
        favorite, created = Favorite.objects.get_or_create(recipe=recipe)
        return favorite

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'recipe', 'reviewer_name', 'rating', 'comment', 'created_at']


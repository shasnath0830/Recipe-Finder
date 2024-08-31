from django.shortcuts import render
from rest_framework import generics
from .models import Recipe, Favorite, Review
from .serializers import RecipeSerializer, FavoriteSerializer, ReviewSerializer
from django.http import HttpResponse
from django.db.models import Q  
from .serializers import RecipeSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class RecipeListView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        ingredients = self.request.query_params.get('ingredients')
        if ingredients:
            ingredient_list = ingredients.split(',')
            query = Q()
            for ingredient in ingredient_list:
                # case-insensitive
                query |= Q(ingredients__iregex=r'\b{}\b'.format(ingredient.strip()))
            queryset = queryset.filter(query).distinct()

        print("Filtered Queryset: ", queryset)  # Debugging line

        return queryset

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class FavoriteListView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteDetailView(generics.RetrieveDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

def home(request):
    return HttpResponse("Welcome to the Recipe Finder API")

class ReviewCreateUpdateView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RecipeRatingView(APIView):

    def post(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response({'error': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)

        rating = request.data.get('rating')
        if not rating:
            return Response({'error': 'Rating not provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        recipe.rating = rating
        recipe.save()

        return Response({'message': 'Rating submitted successfully'}, status=status.HTTP_200_OK)

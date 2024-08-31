from django.core.management.base import BaseCommand
from django.core.files import File
from api.models import Recipe
import os

class Command(BaseCommand):
    help = 'Populate the database with sample recipes'

    def handle(self, *args, **kwargs):
        recipes = [
            {
                'name': 'Chicken Curry',
                'description': 'A spicy and savory chicken curry.',
                'ingredients': 'chicken, onions, garlic, curry powder, tomato',
                'instructions': 'Cook the chicken with onions, garlic, and curry powder. Add tomatoes and simmer.',
                'image_path': 'media/images/Chicken_curry.jpg',
            },
            {
                'name': 'Tomato Basil Pasta',
                'description': 'A simple pasta with tomato and basil.',
                'ingredients': 'pasta, tomato, basil, garlic, olive oil',
                'instructions': 'Cook pasta. In a pan, cook garlic in olive oil, add tomatoes and basil, then toss with pasta.',
                'image_path': 'media/images/Chicken_curry2.jpg',
            },
            {
                'name': 'Beef Stroganoff',
                'description': 'A creamy beef and mushroom dish served over noodles.',
                'ingredients': 'beef, mushrooms, onions, sour cream, egg noodles',
                'instructions': 'Cook beef and onions, add mushrooms and sour cream. Serve over egg noodles.',
                'image_path': 'media/images/Beef_stroganoff.jpg',
            },
            {
                'name': 'Vegetable Stir Fry',
                'description': 'A quick and healthy vegetable stir fry.',
                'ingredients': 'broccoli, bell peppers, carrots, soy sauce, garlic',
                'instructions': 'Stir fry vegetables in soy sauce and garlic. Serve with rice.',
                'image_path': 'media/images/Vegetable_stir_fry.jpg',
            },
            {
                'name': 'Fish Tacos',
                'description': 'Crispy fish tacos with fresh salsa.',
                'ingredients': 'fish, tortillas, cabbage, salsa, lime',
                'instructions': 'Fry the fish, assemble tacos with cabbage and salsa. Serve with lime.',
                'image_path': 'media/images/Fish_tacos.jpg',
            },
            {
                'name': 'Chicken Alfredo',
                'description': 'A creamy chicken alfredo pasta.',
                'ingredients': 'chicken, cream, parmesan, fettuccine, garlic',
                'instructions': 'Cook chicken and garlic, add cream and parmesan. Toss with fettuccine.',
                'image_path': 'static/images/Chicken_alfredo.jpg',
            },
            {
                'name': 'Caesar Salad',
                'description': 'A classic Caesar salad with homemade dressing.',
                'ingredients': 'romaine, croutons, parmesan, caesar dressing',
                'instructions': 'Toss romaine with dressing, top with croutons and parmesan.',
                'image_path': 'media/images/Caesar_salad.jpg',
            },
            {
                'name': 'Margherita Pizza',
                'description': 'A classic Margherita pizza with fresh basil.',
                'ingredients': 'pizza dough, tomato, mozzarella, basil',
                'instructions': 'Top dough with tomatoes and mozzarella. Bake and garnish with basil.',
                'image_path': 'media/images/Margherita_pizza.jpg',
            },
            {
                'name': 'BBQ Ribs',
                'description': 'Slow-cooked BBQ ribs with a smoky sauce.',
                'ingredients': 'ribs, BBQ sauce, spices, garlic',
                'instructions': 'Rub ribs with spices, slow-cook, and baste with BBQ sauce.',
                'image_path': 'media/images/BBQ_ribs.jpg',
            },
            {
                'name': 'Greek Salad',
                'description': 'A fresh Greek salad with feta and olives.',
                'ingredients': 'cucumber, tomato, olives, feta, olive oil',
                'instructions': 'Chop vegetables and toss with olive oil and feta.',
                'image_path': 'media/images/Greek_salad.jpg',
            },
            {
                'name': 'Pancakes',
                'description': 'Fluffy pancakes with maple syrup.',
                'ingredients': 'flour, eggs, milk, baking powder, maple syrup',
                'instructions': 'Mix ingredients, cook on griddle, serve with maple syrup.',
                'image_path': 'media/images/Pancakes.jpg',
            },
            {
                'name': 'Chicken Parmesan',
                'description': 'Breaded chicken with marinara sauce and melted cheese.',
                'ingredients': 'chicken, breadcrumbs, marinara, mozzarella',
                'instructions': 'Bread and fry chicken, top with marinara and mozzarella, bake until melted.',
                'image_path': 'media/images/Chicken_parmesan.jpg',
            },
            {
                'name': 'Sushi Rolls',
                'description': 'Homemade sushi rolls with fresh fish and rice.',
                'ingredients': 'sushi rice, nori, fish, cucumber, avocado',
                'instructions': 'Roll sushi rice with nori, fish, and vegetables. Slice and serve.',
                'image_path': 'media/images/Sushi_rolls.jpg',
            },
            {
                'name': 'Lentil Soup',
                'description': 'A hearty lentil soup with vegetables.',
                'ingredients': 'lentils, carrots, celery, onions, broth',
                'instructions': 'Cook lentils with vegetables in broth until tender.',
                'image_path': 'media/images/Lentil_soup.jpg',
            },
            {
                'name': 'Chocolate Cake',
                'description': 'A rich and moist chocolate cake.',
                'ingredients': 'flour, cocoa powder, sugar, eggs, butter',
                'instructions': 'Mix ingredients, bake until set, cool and frost with chocolate icing.',
                'image_path': 'media/images/Chocolate_cake.jpg',
            }
        ]

        for recipe_data in recipes:
            image_path = recipe_data.pop('image_path')
            recipe = Recipe.objects.create(**recipe_data)
            
            if os.path.exists(image_path):  # Check if the image file exists
                with open(image_path, 'rb') as image_file:
                    recipe.image.save(os.path.basename(image_path), File(image_file), save=True)
            else:
                self.stdout.write(self.style.WARNING(f'Image not found for {recipe.name}: {image_path}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 15 recipes'))

The Recipe Finder is a web application allowing users to search recipes by ingredients, allowing them to rate, or mark it as their favorite. The frontend is built using React.js and the backend is backed by Django.

Features
Search Recipes: Where users can enter by entering one or more ingredients and filtering the recipe with the ingredient. This is an API endpoint, it retrieves a list of recipes. An example is 'GET /API/recipes/?ingredients=chicken, tomato'
Rate Recipes: Users can rate from a scale of 1 to 5. 
Favorite Recipes: Users can mark a recipe as a favorite and view them later, and unfavorite whenever. Another API endpoint, this endpoint allows users to mark a recipe as a favorite. An example is POST /api/favorites/. There also the DELETE /API/favorites/<id>/ 
for deleting a favorite recipe.

Overall this web application has a background with a Recipe section and a favorite section. I did not spend much time on the CSS and debugging the image wouldn't work even after a while. With more time I would be able to flesh out a better styled, responsive, 
and functional website.

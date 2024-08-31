"""
URL configuration for Recipe_Finder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import RecipeListView, RecipeDetailView, FavoriteListView, FavoriteDetailView, RecipeRatingView, ReviewCreateUpdateView, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('api/recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('api/favorites/', FavoriteListView.as_view(), name='favorite-list'),
    path('api/favorites/<int:pk>/', FavoriteDetailView.as_view(), name='favorite-detail'),
    path('api/reviews/', ReviewCreateUpdateView.as_view(), name='review-create-update'),
    path('api/recipes/<int:pk>/rate/', RecipeRatingView.as_view(), name='recipe-rate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

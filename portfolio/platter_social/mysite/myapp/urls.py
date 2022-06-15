from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.follow_feed, name='follow_feed'),
    path('add_post/', views.add_post, name='add_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
    path('add_recipe/<int:id>', views.add_recipe, name='add_recipe'),
    path('view_recipe/<int:id>', views.view_recipe, name='view_recipe'),
    path('discover/', views.discover, name='discover'),
    path('search/', views.search_results, name='search'),
    path('recipe_book/', views.recipe_book, name='recipe_book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

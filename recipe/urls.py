from django.urls import path
from . import views

app_name = "recipe"
urlpatterns = [
    path('create/', views.create, name="create"),
    path('save/', views.save, name="save"),
    path('recipe_list/', views.recipe_list, name="recipe_list"),
    path('<int:recipe_id>/details/', views.details, name="details"),
    path('<int:recipe_id>/delete/', views.delete, name="delete"),

]

from django.shortcuts import render
from .models import Recipes
from django.http import HttpResponseRedirect


# Create your views here.
def recipe_list(request):
    recipe = Recipes.objects.all()
    return render(request, "recipe/recipe_list.html", {"recipes": recipe})


def create(request):
    return render(request, "recipe/create.html")


def save(request):
    Recipes.objects.create(recipe_name=request.POST["recipe_name"],
                           ingredients=request.POST["ingredients"],
                           process=request.POST["process"],
                           images=request.POST["images"])
    return HttpResponseRedirect("/recipe/recipe_list")


def details(request, recipe_id):
    recipe_detail = Recipes.objects.get(id=recipe_id)
    return render(request, 'recipe/details.html', {'recipes': recipe_detail})


def delete(request, recipe_id):
    Recipes.objects.get(id=recipe_id).delete()
    return HttpResponseRedirect('/recipe/recipe_list/')

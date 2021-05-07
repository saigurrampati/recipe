from django.shortcuts import render
from .models import Recipes
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout





# Create your views here.
def login_page(request):
    return render(request, "recipe/login.html")


def register_page(request):
    return render(request, "recipe/register.html")

def save_data(request):
    User.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                             email=request.POST['email'])
    return HttpResponseRedirect("/recipe/")


def login_status(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/recipe/recipe_list/")
    else:
        return HttpResponse("<h3>your username and password did not match</h3>")



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

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/recipe/")

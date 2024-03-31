from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def recipes(request):
    if request.method == "POST":
        data=request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        Recipes.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image
        )
        return redirect('recipes')
    queryset = Recipes.objects.all()
    context = {'recipes': queryset}
    return render(request, 'veges/recipes.html', context)

def delete_recipe(request, id):
    queryset = Recipes.objects.get(id = id)
    queryset.delete()
    return redirect('recipes')

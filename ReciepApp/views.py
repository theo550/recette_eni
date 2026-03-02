from django.shortcuts import render, get_object_or_404

from ReciepApp.models import Recipe

recipesList = [
    { "title": "test", "category": "plat", "time": 1} ,
    { "title": "test1", "category": "entrée", "time": 2},
    { "title": "test2", "category": "dessert", "time": 3}
]

# Create your views here.
def recipes(request):
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(title__icontains=request.GET.get('search'))

    if request.GET.get('category'):
        queryset = queryset.filter(category__icontains=request.GET.get('category'))

    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)

def recipe(request, id):
    queryset = get_object_or_404(Recipe, id=id)

    context = { 'recipe': queryset }
    return render(request, 'recipe.html', context)


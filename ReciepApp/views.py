from django.http import Http404
from django.shortcuts import render, get_object_or_404

from ReciepApp.graphql_client import graphql_query
from ReciepApp.models import Recipe

recipesList = [
    { "title": "test", "category": "plat", "time": 1} ,
    { "title": "test1", "category": "entrée", "time": 2},
    { "title": "test2", "category": "dessert", "time": 3}
]

# Create your views here.
def recipes(request):
    search = request.GET.get('search', '')
    category = request.GET.get('category', '')

    query = """
        query GetRecipes($search: String, $category: String) {
            recipes(search: $search, category: $category) {
                id name time description category
            }
        }
    """
    variables = {"search": search, "category": category}
    result = graphql_query(query, variables)

    print("GraphQL result:", result)

    if not result.get("data") or result["data"]["recipes"] is None:
        context = {'recipes': []}
    else:
        context = {'recipes': result["data"]["recipes"]}

    return render(request, 'recipes.html', context)

def recipe(request, id):
    query = """
        query GetRecipe($id: ID!) {
            recipe(id: $id) {
                id name time description category
            }
        }
    """
    result = graphql_query(query, {"id": id})

    if not result.get("data") or result["data"]["recipe"] is None:
        raise Http404

    context = {'recipe': result["data"]["recipe"]}
    return render(request, 'recipe.html', context)


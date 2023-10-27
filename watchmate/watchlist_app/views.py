"""from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
# Create your views here.
def movie_list(request):
    movies=Movie.objects.all() #Querryset
    data={'movie':list(movies.values())}  #Dictionnary
    return(JsonResponse(data))
def movie_detail(request,pk):
    movie=Movie.objects.get(pk=pk) #Querryset
    data={
        'name':movie.name,
        'description':movie.description,
        'active':movie.active
        }  #Dictionnary
    return(JsonResponse(data))
"""
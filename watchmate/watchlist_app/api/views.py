from watchlist_app.models import Movie
from watchlist_app.api.serialzers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view()
def movie_list(request):
   movies=Movie.objects.all()
   serialazer=MovieSerializer(movies)
   return Response(serialazer.data)
@api_view()
def movie_details(request,pk):
    movie=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)
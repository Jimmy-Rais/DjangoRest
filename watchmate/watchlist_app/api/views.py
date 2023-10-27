from watchlist_app.models import Movie
from watchlist_app.api.serialzers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET','POST'])
def movie_list(request):
   if request.method == 'GET':
   
     movies=Movie.objects.all()
     serialazer=MovieSerializer(movies,many=True)
     return Response(serialazer.data)
   if request.method == 'POST':
      serializer=MovieSerializer(data=request.data)
      if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
      else:
       return Response(serialazer.errors)
@api_view()
def movie_details(request,pk):
    movie=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)
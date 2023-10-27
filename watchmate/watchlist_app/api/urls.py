
from django.contrib import admin
from django.urls import path
from watchlist_app.models import Movie
from watchlist_app.api.views import movie_list,movie_details
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', movie_list,name='movie'),
    path('<int:pk>',movie_details,name='movie_detail'),
]

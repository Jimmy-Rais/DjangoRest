
from django.contrib import admin
from django.urls import path
from watchlist_app.models import Movie
from watchlist_app.views import movie_list,movie_detail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', movie_list,name='movie'),
    path('<int:pk>',movie_detail,name='movie_detail'),
]

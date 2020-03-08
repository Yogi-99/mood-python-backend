from django.urls import path
from apis import views

urlpatterns = [
    path('rest-get/', views.RestAPIView.as_view()),
    path('movies/popular', views.PopularMoviesRestAPIView.as_view()),
    path('movies/genre', views.GenreMoviesRestAPIView.as_view()),
]

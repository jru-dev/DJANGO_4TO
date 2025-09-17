from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('users/<str:username>/', views.profile_view, name='profile'),  # cambiado
]


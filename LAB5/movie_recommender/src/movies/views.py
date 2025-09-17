from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, UserProfile
from .recomendations import get_recommendations

def movie_list(request):
    """Lista todas las películas con opción de búsqueda"""
    query = request.GET.get("q")
    movies = Movie.objects.all().order_by('-release_date')

    if query:
        movies = movies.filter(title__icontains=query)

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'query': query
    })


def movie_detail(request, slug):
    """Detalle de una película específica"""
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

@login_required
def profile_view(request, username):
    """Perfil de usuario con sus ratings y recomendaciones"""
    profile = get_object_or_404(UserProfile, user__username=username)
    recommendations = get_recommendations(profile.user, limit=5)
    return render(request, 'movies/profile.html', {
        'profile': profile,
        'recommendations': recommendations
    })

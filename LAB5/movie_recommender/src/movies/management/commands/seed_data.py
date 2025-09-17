import random 
from datetime import date
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from movies.models import (
    Director, Actor, Genre, Movie, MovieActor, UserProfile, Rating
)

class Command(BaseCommand):
    """Command to seed the database with sample data"""
    help = 'Seeds the database with sample data for testing and development'
    
    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Rating.objects.all().delete()
        MovieActor.objects.all().delete()
        Movie.objects.all().delete()
        Director.objects.all().delete()
        Actor.objects.all().delete()
        Genre.objects.all().delete()
        
        # Create sample directors
        self.stdout.write('Creating directors...')
        directors_data = [
            ("Christopher Nolan", date(1970, 7, 30), "British-American filmmaker known for his cerebral, often nonlinear, storytelling."),
            ("Steven Spielberg", date(1946, 12, 18), "American filmmaker, considered one of the founding pioneers of the New Hollywood era."),
            ("Greta Gerwig", date(1983, 8, 4), "American actress and filmmaker known for her roles in mumblecore films."),
            ("Denis Villeneuve", date(1967, 10, 3), "Canadian filmmaker known for his atmospheric, visually striking films."),
        ]
        directors = []
        for name, birth_date, biography in directors_data:
            d = Director(name=name, birth_date=birth_date, biography=biography)
            d.save()
            directors.append(d)
        
        # Create sample actors
        self.stdout.write('Creating actors...')
        actors_data = [
            ("Leonardo DiCaprio", date(1974, 11, 11), "American actor known for his intense, unconventional roles."),
            ("Meryl Streep", date(1949, 6, 22), "American actress often described as the 'best actress of her generation'."),
            ("Tom Hanks", date(1956, 7, 9), "American actor and filmmaker, known for both comedic and dramatic roles."),
            ("Viola Davis", date(1965, 8, 11), "American actress and producer, known for her powerful performances."),
            ("Timothée Chalamet", date(1995, 12, 27), "American actor known for his roles in independent films."),
            ("Saoirse Ronan", date(1994, 4, 12), "Irish and American actress known for her roles in period dramas."),
        ]
        actors = []
        for name, birth_date, biography in actors_data:
            a = Actor(name=name, birth_date=birth_date, biography=biography)
            a.save()
            actors.append(a)
        
        # Create sample genres
        self.stdout.write('Creating genres...')
        genres_data = [
            ("Action", "Action films emphasize spectacular physical action."),
            ("Comedy", "Comedy films are designed to provoke laughter."),
            ("Drama", "Drama films are serious in tone, focusing on personal development."),
            ("Science Fiction", "Science fiction films deal with imaginative and futuristic concepts."),
            ("Horror", "Horror films seek to elicit fear or disgust from the audience."),
            ("Romance", "Romance films focus on love and romantic relationships."),
            ("Thriller", "Thriller films maintain high levels of suspense and excitement."),
        ]
        genres = []
        for name, description in genres_data:
            g = Genre(name=name, description=description)
            g.save()
            genres.append(g)
        
        # Create sample movies
        self.stdout.write('Creating movies...')
        movies_data = [
            ("Inception", date(2010, 7, 16), "A thief who steals corporate secrets through dream-sharing.", 148, directors[0], [genres[3], genres[6]]),
            ("Jurassic Park", date(1993, 6, 11), "Dinosaurs escape in a theme park.", 127, directors[1], [genres[0], genres[3]]),
            ("Little Women", date(2019, 12, 25), "The lives of the March sisters in 19th-century Massachusetts.", 135, directors[2], [genres[2], genres[5]]),
            ("Dune", date(2021, 10, 22), "A noble family fights for control of a valuable resource.", 155, directors[3], [genres[0], genres[3]]),
            ("Interstellar", date(2014, 11, 7), "Explorers travel through a wormhole to save humanity.", 169, directors[0], [genres[2], genres[3]]),
        ]
        movies = []
        for title, release_date, plot, runtime, director, genre_list in movies_data:
            m = Movie(title=title, release_date=release_date, plot=plot, runtime=runtime, director=director)
            m.save()
            m.genres.add(*genre_list)
            movies.append(m)
        
        # Create MovieActor relationships
        self.stdout.write('Creating movie-actor relationships...')
        movie_actors = [
            MovieActor(movie=movies[0], actor=actors[0], character_name="Dom Cobb", is_lead=True),
            MovieActor(movie=movies[1], actor=actors[2], character_name="Dr. Alan Grant", is_lead=True),
            MovieActor(movie=movies[2], actor=actors[5], character_name="Jo March", is_lead=True),
            MovieActor(movie=movies[2], actor=actors[4], character_name="Laurie", is_lead=False),
            MovieActor(movie=movies[3], actor=actors[4], character_name="Paul Atreides", is_lead=True),
            MovieActor(movie=movies[4], actor=actors[0], character_name="Cooper", is_lead=True),
        ]
        for ma in movie_actors:
            ma.save()
        
        # Create users + profiles
        self.stdout.write('Creating users...')
        users = []
        for i in range(1, 6):
            username = f"user{i}"
            user = User.objects.create_user(
                username=username,
                email=f"{username}@example.com",
                password="password123"
            )
            users.append(user)
            profile = UserProfile.objects.create(user=user, bio=f"Bio for {username}")
            profile.favorite_genres.add(*random.sample(genres, 2))
        
        # Create ratings
        self.stdout.write('Creating ratings...')
        for user in users:
            for movie in random.sample(movies, random.randint(2, 4)):
                rating = Rating(
                    user=user,
                    movie=movie,
                    value=random.randint(1, 10),
                    comment=f"Rating comment from {user.username} for {movie.title}"
                )
                rating.save()
        
        # Update average ratings
        for movie in movies:
            if hasattr(movie, "update_avg_rating"):
                movie.update_avg_rating()
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))

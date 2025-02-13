from . import views
from .models import Movie
from django.shortcuts import render

def generate_movies_context():
    context = {}
    # Show only movies in recommendation list
    # Sorted by vote_average in desc
    # Get recommended movie counts
    recommended_count = Movie.objects.filter(recommended=True).count()
    # If there are no recommended movies
    if recommended_count == 0:
        # Just return the top voted and unwatched movies as popular ones
        movies = Movie.objects.filter(watched=False).order_by('-vote_average')[:30]
    else:
        # Get the top voted, unwatched, and recommended movies
        movies = Movie.objects.filter(watched=False).filter(recommended=True).order_by('-vote_average')[:30]
    context['movie_list'] = movies
    return context

# HINT: Create a view to provide movie recommendations list for the HTML template
def movie_recommendation_view(request):
    if request.method == 'GET':
        # HINT: Get the movie recommendations from the database
        context = generate_movies_context()
        # Render the HTML template with the movie recommendations
        return render(request, 'movierecommender/movie_list.html', context)


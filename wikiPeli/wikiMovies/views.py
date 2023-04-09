from django.shortcuts import render
from .forms import InsertForm, SearchForm
from .models import Movie


# Create your views here.


def home(request):
    return render(request, 'home.html')

def insert_movie(request):
    if request.method == 'POST':
        form = InsertForm(request.POST)
        if form.is_valid():
            movie = Movie(title=form.cleaned_data['title'],
                          year=form.cleaned_data['year'],
                          director=form.cleaned_data['director'])
            movie.save()
            movie.genres.set(form.cleaned_data['genres'])
    else:
        form = InsertForm()
    return render(request, 'insert_movies.html', {'form': form})

def search_movie(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            movies = Movie.objects.filter(title__icontains=form.cleaned_data['title'],
                                          year=form.cleaned_data['year'],
                                          director=form.cleaned_data['director'],
                                          genres__in=form.cleaned_data['genres'])
    else:
        form = SearchForm()
        movies = Movie.objects.all()
    return render(request, 'search_movie.html', {'form': form, 'movies': movies})

from django import forms
from .models import Genre, Director, Movie

#Formulario de ingreso
class InsertForm(forms.Form):
    title = forms.CharField(max_length=200)
    year = forms.IntegerField()
    director = forms.ModelChoiceField(queryset=Director.objects.all())
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all())

#Formulario de búsqueda
class SearchForm(forms.Form):
    title = forms.CharField(required=False)
    year = forms.IntegerField(required=False)
    director = forms.ModelChoiceField(queryset=Director.objects.all(), required=False)
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), required=False)

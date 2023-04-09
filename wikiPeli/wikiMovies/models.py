from django.db import models

# Create your models here

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

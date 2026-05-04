from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', verbose_name='Author', help_text='Author')
    year_published = models.SmallIntegerField(
        validators=[MaxValueValidator(timezone.now().year)],
        help_text='Year published. For years BC use negative numbers'
    )
    description = models.TextField()
    genres = models.ManyToManyField('Genre', related_name='books', verbose_name='Genre')

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    birth_date = models.DateField(
        help_text='Date of birth. BC years are available'
    )


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Genre(models.Model):
    name = models.CharField(max_length=100)
    brief_description = models.TextField()

    def __str__(self):
        return f'{self.name}'


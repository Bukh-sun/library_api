from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import TextInput

from library.models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.DateField: {'widget': TextInput(attrs={'placeholder': 'YYYY-MM-DD'})},
    }

admin.site.register(Genre)


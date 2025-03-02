from django.contrib import admin

from .models import MoviePerson, Movie, MovieReview,  Genre


admin.site.register(Movie)
admin.site.register(MoviePerson)
admin.site.register(MovieReview)
admin.site.register(Genre)

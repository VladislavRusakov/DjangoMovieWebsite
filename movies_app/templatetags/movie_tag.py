from django import template

from movies_app.models import Category, Movie


register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag("tags/last_movie.html")
def get_last_movies(count=5):
    movies = Movie.objects.order_by("-id")[:count]
    print({"last_movies": movies})
    print()
    return {"last_movies": movies}

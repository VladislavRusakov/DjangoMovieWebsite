from django.contrib import admin
from django.utils.html import mark_safe

from .models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "id")

class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 0
    readonly_fields = ("email", "name", "parent")

class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 0
    readonly_fields = ("get_image", "movie")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="200" height="220"')

    get_image.short_description = "Изображение"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category","year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline ,ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    fieldsets = (
        ("Main", {
            "fields": (("title", "tagline"), )
        }),
        ("Text and IMG", {
            "classes":("collapse", ),
            "fields": (("description", ("poster", "get_image")) )
        }),
        ("Dates and places", {
            "fields": (("year", "world_premiere", "country"), )
        }),
        ("People and genres", {
            "fields": (("actors", "directors", "genre", "category"), )
        }),
        ("Money", {
            "fields": (("budget", "fees_in_usa", "fees_in_world"), )
        }),
        ("Options", {
            "fields": (("url","trailer_url", "draft"), )
        })
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="300" height="330"')

    get_image.short_description = "Постер"

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id",)
    readonly_fields = ("email", "name")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)
    list_display_links = ("name", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = "Изображение"

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("movie", "ip", "star")

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)
    list_display_links = ("title", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = "Изображение"

admin.site.register(RatingStar)

admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"
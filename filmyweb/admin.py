from django.contrib import admin
from .models import Film


# - pierwszy sposób
# admin.site.register(Film)
# - drugi sposób :
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis","rok"] # rejestrowane pola w django admin
    # exclude = ["opis"] # wszystko poza opisem
    list_display = ["tytul", "imdb_rating", "rok"]
    list_filter = ("rok", "opis")
    search_fields = ("tytul", "opis", )
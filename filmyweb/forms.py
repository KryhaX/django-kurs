from django.forms import ModelForm
from .models import Film
from django import forms

class FilmForm(ModelForm):
    class Meta:
        model = Film # Jaki model bedziemy uzywac
        fields = ['tytul','opis','premiera','rok','imdb_rating','plakat']# Jaki fields bedziemy uzywac
        widgets = {
            'opis': forms.Textarea(attrs={'class': 'opis-field'})
        }
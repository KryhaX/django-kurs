from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required


def wszystkie_filmy(request):
    test = 'To jest zmienna w filmyweb/views.py'
    lista_filmow = ['Avatar', 'Titanic', 'Wejscie smoka']
    filmyweb = Film.objects.all()
    username = request.user.username
    return render(request, 'filmy.html', {'text': test, 'lista_filmow': lista_filmow, 'film_z_rokiem': filmyweb, 'username':username,})

# sam wymyslilem xD
def cwiczenie(request):
    return render(request, 'cwiczenie.html')

@login_required
def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)


    return render(request, 'film_form.html', {'form': form})

@login_required
def edytuj_film(request, id):
    film = get_object_or_404(Film,pk = id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form})

@login_required
def usun_film(request, id):
    film = get_object_or_404(Film,pk = id)

    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': film})
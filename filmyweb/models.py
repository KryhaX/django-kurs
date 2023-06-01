from django.db import models


class Film(models.Model):
    tytul = models.CharField(max_length=64, blank=False, unique=True)
    rok = models.PositiveSmallIntegerField(default=2000)
    opis = models.TextField(max_length=255, blank=True, unique=False)
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=1)
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True)

    # Zmiana nazwy obiektów filmy
    def __str__(self):
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul,self.rok)

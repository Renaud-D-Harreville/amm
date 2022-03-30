from django.db import models


class RegimeAlimentaire(models.Model):

    name = models.CharField(max_length=64, unique=True)
    short_description = models.TextField()
    long_description = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Animal(models.Model):

    name = models.CharField(max_length=64, unique=True)
    short_description = models.TextField()
    long_description = models.TextField()
    regime_alimentaire = models.ForeignKey(RegimeAlimentaire, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


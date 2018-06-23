from django.db import models

# https://docs.djangoproject.com/en/2.0/topics/db/models/
# https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/

class Movie(models.Model):
    id_movie = models.IntegerField()
    title = models.CharField(max_length=200, null=False)
    overview = models.CharField(max_length=2000, null=False)
    date = models.DateField(null=False)
    director = models.CharField(max_length=100, null=False)
    url_poster = models.CharField(max_length=300, null=False)
    vote_average = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    url_video = models.CharField(max_length=300)
    budget = models.DecimalField(max_digits=100, decimal_places=2)
    revenue = models.DecimalField(max_digits=100, decimal_places=2)
    original_language = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Cast(models.Model):
    name = models.CharField(max_length=100, null=False)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
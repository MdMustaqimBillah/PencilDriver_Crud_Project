from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    artist_age = models.IntegerField()

    def __str__(self):
        return self.first_name + '' + self.last_name + '' + f'( {self.artist_age} )'
    

class Album(models.Model):
    name = models.ForeignKey(Musician, on_delete = models.CASCADE)
    album_title = models.CharField(max_length=25)
    release_date = models.DateField()
    stars = ((1,'Worst'),
             (2,'Bad'),
             (3,'Average'),
             (4,'Good'),
             (5,'Best')
             )
    album_ratings = models.IntegerField(choices=stars)

    def __str__(self):
        return self.title + " " + f'({"★" * self.ratings })'
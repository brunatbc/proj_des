from django.db import models

# Create your models here.

class Musica (models.Model):
    name = models.CharField('name',max_length = 30 )
    author = models.CharField('author', max_length = 50)
    desc = models.CharField('desc', max_length = 500)



class Album (models.Model):
    VERSION_CHOICES = (
        ("Standard","Standard"),
        ("Deluxe","Deluxe"),
    )
    name = models.CharField('name',max_length = 30 )
    author = models.CharField('author', max_length=50)
    version = models.CharField(max_length=20, choices=VERSION_CHOICES)
    desc = models.CharField('desc', max_length=500)

    def __str__(self):
        return self.name



class Artist (models.Model):
    name = models.CharField('name',max_length = 50 )
    age = models.IntegerField('age')
    nationality =  models.CharField('nationality',max_length = 100 )


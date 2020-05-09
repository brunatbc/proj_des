from django.contrib import admin
from .models import Musica
from .models import Album
from .models import Artist

# Register your models here.

class MusicaAdmin (admin.ModelAdmin):
    list_display = ('name', 'author','desc')

admin.site.register(Musica)

class AlbumAdmin (admin.ModelAdmin):
    list_display = ('name','author','version','desc')

admin.site.register(Album)

class ArtistAdmin (admin.ModelAdmin):
    list_display = ('name','age','nationality')

admin.site.register(Artist)




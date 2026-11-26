from django.contrib import admin
from .models import Genero, Filme


admin.site.register(Genero)


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ["titulo", "diretor", "ano", "assistido", "genero"]
from django.shortcuts import render, redirect, get_object_or_404
from .models import Genero, Filme
from .forms import FilmeForm


def filmes(request):
    dados = {"filmes": Filme.objects.all()}
    return render(request, "filmes.html", dados)


def novo_filme(request):
    if request.method == "POST":
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/filmes/")
    else:
        form = FilmeForm()
    return render(request, "form_filme.html", {"form": form, "titulo": "Novo filme"})


def detalhe_filme(request, id):
    item = get_object_or_404(Filme, id=id)
    return render(request, "detalhe_filme.html", {"item": item})


def editar_filme(request, id):
    item = get_object_or_404(Filme, id=id)
    if request.method == "POST":
        form = FilmeForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/filmes/")
    else:
        form = FilmeForm(instance=item)
    return render(request, "form_filme.html", {"form": form, "titulo": "Editar filme"})


def excluir_filme(request, id):
    item = get_object_or_404(Filme, id=id)
    if request.method == "POST":
        item.delete()
        return redirect("/filmes/")
    return render(request, "excluir_filme.html", {"item": item})
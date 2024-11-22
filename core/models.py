from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey("Author", related_name="books", on_delete=models.CASCADE)
    categoria = models.ForeignKey(
        "Categoria", related_name="books", on_delete=models.CASCADE
    )
    publicado_em = models.DateField()

    def __str__(self):
        return self.title


class Colecao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    livros = models.ManyToManyField(Book, related_name="colecoes")
    colecionador = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="colecoes"
    )

    def __str__(self):
        return f"{self.nome} - {self.colecionador.username}"

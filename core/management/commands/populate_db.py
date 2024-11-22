from django.core.management.base import BaseCommand
from core.models import Categoria, Author, Book

class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        categoria_misterio = Categoria.objects.create(name="Mistério")
        categoria_ficcao = Categoria.objects.create(name="Ficção")
        categoria_fantasia = Categoria.objects.create(name="Fantasia")
        categoria_romance = Categoria.objects.create(name="Romance")

        autor_agatha_christie = Author.objects.create(name="Agatha Christie", birth_date="1890-09-15")
        autor_arthur_c_clarke = Author.objects.create(name="Arthur C. Clarke", birth_date="1917-12-16")
        autor_arthur_conan_doyle = Author.objects.create(name="Arthur Conan Doyle", birth_date="1859-05-22")
        autor_cs_lewis = Author.objects.create(name="C.S. Lewis", birth_date="1898-11-29")
        autor_emily_bronte = Author.objects.create(name="Emily Brontë", birth_date="1818-07-30")
        autor_george_rr_martin = Author.objects.create(name="George R.R. Martin", birth_date="1948-09-20")
        autor_isaac_asimov = Author.objects.create(name="Isaac Asimov", birth_date="1920-01-02")
        autor_jrr_tolkien = Author.objects.create(name="J.R.R. Tolkien", birth_date="1892-01-03")

        Book.objects.create(
            title="Assassinato no Expresso do Oriente",
            author=autor_agatha_christie,
            categoria=categoria_misterio,
            publicado_em="1934-01-01",
        )
        Book.objects.create(
            title="Morte no Nilo",
            author=autor_agatha_christie,
            categoria=categoria_misterio,
            publicado_em="1937-11-01",
        )
        Book.objects.create(
            title="2001: Uma Odisseia no Espaço",
            author=autor_arthur_c_clarke,
            categoria=categoria_ficcao,
            publicado_em="1968-06-16",
        )
        Book.objects.create(
            title="Encontro com Rama",
            author=autor_arthur_c_clarke,
            categoria=categoria_ficcao,
            publicado_em="1973-06-01",
        )
        Book.objects.create(
            title="O Cão dos Baskervilles",
            author=autor_arthur_conan_doyle,
            categoria=categoria_misterio,
            publicado_em="1902-04-01",
        )
        Book.objects.create(
            title="Um Estudo em Vermelho",
            author=autor_arthur_conan_doyle,
            categoria=categoria_misterio,
            publicado_em="1887-11-01",
        )
        Book.objects.create(
            title="As Crônicas de Nárnia",
            author=autor_cs_lewis,
            categoria=categoria_fantasia,
            publicado_em="1950-10-16",
        )
        Book.objects.create(
            title="O Leão, a Feiticeira e o Guarda-Roupa",
            author=autor_cs_lewis,
            categoria=categoria_fantasia,
            publicado_em="1950-10-16",
        )
        Book.objects.create(
            title="O Morro dos Ventos Uivantes",
            author=autor_emily_bronte,
            categoria=categoria_romance,
            publicado_em="1847-12-01",
        )
        Book.objects.create(
            title="A Guerra dos Tronos",
            author=autor_george_rr_martin,
            categoria=categoria_fantasia,
            publicado_em="1996-08-06",
        )
        Book.objects.create(
            title="A Fúria dos Reis",
            author=autor_george_rr_martin,
            categoria=categoria_fantasia,
            publicado_em="1998-11-16",
        )
        Book.objects.create(
            title="Fundação",
            author=autor_isaac_asimov,
            categoria=categoria_ficcao,
            publicado_em="1951-06-01",
        )
        Book.objects.create(
            title="Eu, Robô",
            author=autor_isaac_asimov,
            categoria=categoria_ficcao,
            publicado_em="1950-12-02",
        )
        Book.objects.create(
            title="O Senhor dos Anéis",
            author=autor_jrr_tolkien,
            categoria=categoria_fantasia,
            publicado_em="1954-07-29",
        )
        Book.objects.create(
            title="O Hobbit",
            author=autor_jrr_tolkien,
            categoria=categoria_fantasia,
            publicado_em="1937-09-21",
        )
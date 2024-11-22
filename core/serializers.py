from rest_framework import serializers
from .models import Book, Author, Categoria, Colecao


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="book-detail",
    )

    class Meta:
        model = Categoria
        fields = ["url", "id", "name", "books"]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField()

    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="book-detail",
    )

    class Meta:
        model = Author
        fields = ["url", "id", "name", "birth_date", "books"]


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)

    # Para envio dos dados (criação e atualização)
    categoria = serializers.SlugRelatedField(
        queryset=Categoria.objects.all(), slug_field="name"
    )
    author = serializers.HyperlinkedRelatedField(
        view_name="author-detail", queryset=Author.objects.all()
    )

    # Para exibição apenas do campo 'name' nas respostas
    author_name = serializers.CharField(source="author.name", read_only=True)

    publicado_em = serializers.DateField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.categoria = validated_data.get("categoria", instance.categoria)
        instance.publicado_em = validated_data.get(
            "publicado_em", instance.publicado_em
        )
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = [
            "url",
            "id",
            "title",
            "author",
            "author_name",
            "categoria",
            "publicado_em",
        ]


class ColecaoSerializer(serializers.ModelSerializer):
    livros = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), many=True)

    class Meta:
        model = Colecao
        fields = ["id", "nome", "descricao", "livros", "colecionador"]
        read_only_fields = ["colecionador"]

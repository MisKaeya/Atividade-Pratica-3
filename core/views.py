from rest_framework import generics, permissions, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from core.models import Categoria, Author, Book, Colecao
from core.serializers import (
    CategoriaSerializer,
    AuthorSerializer,
    LivroSerializer,
    ColecaoSerializer,
)
from core.filters import BookFilter, AuthorFilter
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomPermission
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class EmptySerializer(serializers.Serializer):
    pass


class APIRootView(APIView):
    name = "api-root"
    serializer_class = EmptySerializer

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "categorias": reverse(CategoriaList.name, request=request),
                "authors": reverse(AuthorList.name, request=request),
                "books": reverse(BookList.name, request=request),
                "colecao": reverse(ColecaoListCreate.name, request=request),
            }
        )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        return user


@extend_schema(
    summary="Criar novo usuário",
    description="Endpoint para criar um novo usuário. Envie 'username' e 'password' para registrar um novo usuário.",
    examples=[
        OpenApiExample(
            "Exemplo de requisição",
            value={"username": "novo_usuario", "password": "senha123"},
            request_only=True,
        ),
        OpenApiExample(
            "Exemplo de resposta",
            value={"id": 1, "username": "novo_usuario"},
            response_only=True,
        ),
    ],
)
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(
    summary="Obter Token de Autenticação",
    description="Endpoint para obter um token de autenticação. Envie 'username' e 'password' como JSON para receber o token.",
    examples=[
        OpenApiExample(
            "Exemplo de requisição",
            value={"username": "usuario", "password": "senha"},
            request_only=True,
        ),
        OpenApiExample(
            "Exemplo de resposta",
            value={"token": "seu_token_aqui"},
            response_only=True,
        ),
    ],
)
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ("^name",)
    ordering_fields = ("name",)
    name = "categoria-list"


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter
    name = "author-list"


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = "author-detail"


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = LivroSerializer
    filterset_class = BookFilter
    search_fields = ("^title",)  # Aqui é importante a virgula
    ordering_fields = ("title", "author", "categoria", "publicado_em")
    name = "book-list"


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = LivroSerializer
    name = "book-detail"


class ColecaoListCreate(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsAuthenticated]
    name = "colecao-list-create"

    def perform_create(self, serializer):
        # Associa o colecionador como o usuário autenticado
        serializer.save(colecionador=self.request.user)


class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [permissions.IsAuthenticated, CustomPermission]
    name = "colecao-detail"

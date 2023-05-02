from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Editora, Livro
from livraria.serializers import CategoriaSerializer, EditoraSerializer, LivroDetailSerializer, LivroSerializer, LivroListSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    serializer_classes = {
        "list": LivroListSerializer,
        "retrieve": LivroDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LivroSerializer)
    

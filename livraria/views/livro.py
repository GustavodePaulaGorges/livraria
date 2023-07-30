from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from livraria.models import Livro
from livraria.serializers import LivroDetailSerializer, LivroSerializer, LivroListSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    serializer_classes = {
        "list": LivroListSerializer,
        "retrieve": LivroDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LivroSerializer)
    

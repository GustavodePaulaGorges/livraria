from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from livraria.models import Autor
from livraria.serializers import AutorSerializer

class AutorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
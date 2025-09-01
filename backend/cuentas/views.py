from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

from .models import ClienteEsctop
from rest_framework.generics import ListAPIView
from .serializers import ClienteEsctopSerializer

class ClienteEsctopListView(ListAPIView):
    queryset = ClienteEsctop.objects.all()
    serializer_class = ClienteEsctopSerializer

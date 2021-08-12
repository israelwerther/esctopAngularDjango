from .models import ClienteCredcoop
from rest_framework.generics import ListAPIView
from .serializers.credcoopserializers import ClienteCredcoopSerializer
class ClienteCreedcoopListView(ListAPIView):
    queryset = ClienteCredcoop.objects.all()
    serializer_class = ClienteCredcoopSerializer
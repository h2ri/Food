from rest_framework import viewsets
from .serializers import ItemSerializers
from .models import Items

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializers
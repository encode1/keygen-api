from rest_framework.generics import ListCreateAPIView, DestroyAPIView

from .models import Key
from .serializers import KeySerializer


class KeyList(ListCreateAPIView):
    queryset = Key.objects.all()
    serializer_class = KeySerializer


class KeyDestroy(DestroyAPIView):
    queryset = Key.objects.all()

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()

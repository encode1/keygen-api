from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response

from .models import Key
from .serializers import KeySerializer


class KeyList(ListCreateAPIView):
    queryset = Key.objects.all()
    serializer_class = KeySerializer


class KeyDestroy(DestroyAPIView):
    queryset = Key.objects.all()

    def perform_destroy(self, instance):
        print(isinstance(instance, Key))
        instance.deleted = True
        instance.save()

from django.urls import path

from .apiviews import KeyList, KeyDestroy

urlpatterns = [
    path('keys/', KeyList.as_view(), name='key_list'),
    path('keys/<int:pk>/', KeyDestroy.as_view(), name='key_delete'),
]
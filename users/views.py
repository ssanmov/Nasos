from .serializers import *
from rest_framework import viewsets


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filterset_fields = '__all__'
    search_fields = ['user']




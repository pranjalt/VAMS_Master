from rest_framework import generics
from restapp.serializers import AlbumSerializer
from models import Album

class Album(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

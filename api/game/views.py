from game.models import Post, Version, Game
from rest_framework import generics, viewsets, filters
from rest_framework.response import Response
from .serializers import PostSerializer, VersionSerializer


class GameViewSet(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        version = Version.objects.last()
        game = Game.objects.first()
        response = {
            "version": version.slug,
            "url": game.download if game else "",
            "redirect": version.pk,
            "date": version.created
        }
        return Response(response)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    http_method_names = ['get']
    permission_classes = []

    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    http_method_names = ['get']
    permission_classes = []

    filter_backends = [filters.SearchFilter]
    search_fields = ['slug']

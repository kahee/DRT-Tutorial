from rest_framework import generics, permissions, renderers
from rest_framework.response import Response

from ..permissions import IsOwnerOrReadOnly
from ..models import Snippet
from ..serializers import SnippetSerializer

__all__ = (
    'SnippetList',
    'SnippetDetail',
    'SnippetHighlight',
)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # 인증 받은 사람들은 읽기와 쓰기 권한 주어지고 아니면 오직 읽기만 주어짐
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (
        renderers.StaticHTMLRenderer,
    )

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


from rest_framework import generics, permissions

from ..permissions import IsOwnerOrReadOnly
from ..models import Snippet
from ..serializers import SnippetSerializer

__all__ = (
    'SnippetList',
    'SnippetDetail',
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




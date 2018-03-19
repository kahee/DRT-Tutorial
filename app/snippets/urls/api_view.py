from rest_framework.urlpatterns import format_suffix_patterns

from ..apis.api_view import SnippetList, SnippetDetail
from django.urls import path

urlpatterns = [
    path('', SnippetList.as_view(), name='snippets-list'),
    path('<int:pk>/', SnippetDetail.as_view(), name='snippet-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

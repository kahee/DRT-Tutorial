from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from django.urls import path

app_name = 'snippets'
urlpatterns = [
    path('', views.SnippetList.as_view(), name='snippets-list'),
    path('<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
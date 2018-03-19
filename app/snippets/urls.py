from . import views
from django.urls import path

app_name = 'snippets'
urlpatterns = [
    path('', views.SnippetList.as_view(), name='snippets-list')
]

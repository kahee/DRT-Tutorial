from django.urls import path, include

app_name = 'snippets'
urlpatterns = [
    path('api-view/', include('snippets.urls.api_view')),
]

from django.urls import path, include

urlpatterns = [
    path('api-view/', include('snippets.urls.api_view')),
    path('mixins/', include('snippets.urls.mixins')),
    path('generic/', include('snippets.urls.generic')),
    path('viewsets/', include('snippets.urls.viewsets')),
    path('routers/', include('snippets.urls.routers')),
]

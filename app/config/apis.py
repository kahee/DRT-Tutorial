from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIRoot(APIView):
    def get(self, request, format=None):
        data = {
            # reverse urlname -> url을 만드는 것
            'users': reverse('user-list', request=request, format=format),
            'snippets': reverse('snippet-list', request=request, format=format)
        }

        return Response(data)

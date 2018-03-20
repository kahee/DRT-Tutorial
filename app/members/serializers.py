from django.contrib.auth import get_user_model
from rest_framework import serializers

from snippets.models import Snippet

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='snippets:snippet-detail',
        read_only=True,
    )

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'snippets',
        )

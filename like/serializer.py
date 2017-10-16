from rest_framework import serializers

from like.models import Like


class LikeSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Like
        fields = ('author', 'created', 'updated', 'content_type',
                  'object_id')

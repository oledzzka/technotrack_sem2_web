from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('author', 'title', 'created', 'updated', 'photo')


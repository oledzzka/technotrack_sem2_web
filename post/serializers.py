from rest_framework import serializers

from core.models import User
from post.models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'username', 'id']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('author', 'title', 'created', 'updated', 'photo', 'id', 'likes_count')


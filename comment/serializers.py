from rest_framework import serializers

from comment.models import Comment
from core.serializers import ContentObjectSerializer
from post.models import Post
from post.serializers import PostSerializer


class CommentedSerializer(ContentObjectSerializer):

    def to_representation(self, value):
        if isinstance(value, Post):
            serializer = PostSerializer(value)
        else:
            return None
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    content_object = CommentedSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("author", "created", "updated", "text", "content_object")


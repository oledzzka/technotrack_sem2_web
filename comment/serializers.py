from rest_framework import serializers

from comment.models import Comment
from core.serializers import ContentObjectSerializer
from post.models import Post
from post.serializers import PostSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ("author", "created", "updated", "text",
                  "content_type", "object_id")


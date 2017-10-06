from rest_framework import serializers

from comment.models import Comment
from comment.serializers import CommentSerializer
from core.serializers import ContentObjectSerializer
from like.models import Like
from post.models import Post
from post.serializers import PostSerializer


class LikedSerializer(ContentObjectSerializer):

    def to_internal_value(self, data):
        # t = super(LikedSerializer, self).to_internal_value()
        # c
        pass

    def to_representation(self, value):
        if isinstance(value, Post):
            serializer = PostSerializer(value)
        elif isinstance(value, Comment):
            serializer = CommentSerializer(value)
        else:
            return None
        return serializer.data

    def get_queryset(self):
        qs = []
        for post in Post.objects.all().values():
            qs.append(post)
        return qs


class LikeSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    content_object = LikedSerializer()
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Like
        fields = ('author', 'created', 'updated', 'content_object')

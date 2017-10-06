from rest_framework import serializers

from comment.models import Comment
from comment.serializers import CommentSerializer
from core.serializers import ContentObjectSerializer
from event.models import Event
from like.models import Like
from like.serializer import LikeSerializer
from post.models import Post
from post.serializers import PostSerializer


class ObjectEventSerializer(ContentObjectSerializer):

    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        if isinstance(value, Post):
            serializer = PostSerializer(value)
        elif isinstance(value, Comment):
            serializer = CommentSerializer(value)
        elif isinstance(value, Like):
            serializer = LikeSerializer
        else:
            return None
        return serializer.data


class EventSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    object_event = ObjectEventSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('author', 'text', 'created', 'updated', 'object_event')


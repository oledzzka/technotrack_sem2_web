from rest_framework import serializers

from event.models import Event


class EventSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = ('author', 'text', 'created', 'updated', 'content_type', 'object_id')

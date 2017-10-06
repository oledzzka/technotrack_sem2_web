from rest_framework import serializers

from core.models import User


class ContentObjectSerializer(serializers.RelatedField):

    def to_representation(self, value):
        raise NotImplementedError()


class OtherUserSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField()
    last_name = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    avatar = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'avatar')


class SelfUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
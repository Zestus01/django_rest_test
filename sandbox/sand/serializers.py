from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sand.models import Sand, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES)
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    kinetic = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Sand` isntance
        """
        return Sand.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Sand` instance
        """
        instance.title = validated_data.get('title', instance.title)
        instance.kinetic = validated_data.get('kinetic', instance.kinetic)
        instance.style = validated_data.get('style', instance.style)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance
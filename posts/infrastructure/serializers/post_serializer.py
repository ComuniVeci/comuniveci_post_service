from rest_framework import serializers
from posts.domain.models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True, source="_id")
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    address = serializers.CharField(required=False)
    contact_email = serializers.EmailField(required=False)
    images = serializers.ListField(child=serializers.URLField(), required=False)
    is_approved = serializers.BooleanField(required=False)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post(**validated_data).save()
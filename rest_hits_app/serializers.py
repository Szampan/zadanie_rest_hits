from rest_framework import serializers
from .models import Artist, Hit

class HitSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Hit
        fields = ['id', 'title', 'artist', 'title_url', 'created_at', 'updated_at']




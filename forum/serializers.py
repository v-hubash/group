from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    views_count = serializers.IntegerField(read_only=True)
    total_likes = serializers.IntegerField(read_only=True)
    total_dislikes = serializers.IntegerField(read_only=True)

    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'content', 'image_url', 'author_username', 'views_count', 'total_likes', 'total_dislikes','created_at']


    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None
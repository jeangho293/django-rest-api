from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)

    class Meta:
        model = Post
        fields = ["id", "title", "content"]

    @staticmethod
    def find_all():
        return Post.manager.find_all()

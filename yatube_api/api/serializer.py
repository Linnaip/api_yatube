from rest_framework import serializers
from posts.models import Post, Group, Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    group = serializers.SlugRelatedField(slug_field='slug', read_only=True, required=False)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment

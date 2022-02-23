from rest_framework import serializers
from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'slug', 'title', 'author', 'excerpt', 'content', 'status')
        model = Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Category
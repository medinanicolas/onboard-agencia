from .models import Post
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class PostSerializer(serializers.ModelSerializer):
    post_title = serializers.CharField(required=True, min_length=4, validators=[UniqueValidator(queryset=Post.objects.all(), message="Este post ya existe")])
    class Meta:
        model = Post
        fields = '__all__'
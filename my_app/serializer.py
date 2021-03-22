from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'blog', 'body', 'created_at') # reference your models.py for these fields
        model = Blog
from rest_framework import serializers
from .models import User,Posts

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password')
class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id','username', 'description', 'time')
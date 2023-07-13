from rest_framework import serializers

from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(source='userprofile', many=False)

    class Meta:
        model = User
        fields = ('email', 'password') # , 'profile')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
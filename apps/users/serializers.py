from rest_framework import serializers

from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='userprofile', many=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
    
    # Custom .update() method for serializer to handle UserProfile data update
    def update(self, instance, validated_data):
        userprofile_serializer = self.fields['profile']
        userprofile_instance = instance.userprofile
        userprofile_data = validated_data.pop('userprofile', {})

        # to access the UserProfile fields in here
        # mobile = userprofile_data.get('mobile')

        # update the userprofile fields
        userprofile_serializer.update(userprofile_instance, userprofile_data)

        instance = super().update(instance, validated_data)
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import CustomUser
from actions.serializers import DiarySerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    recent = DiarySerializer(many=True)
    class Meta:
        model = CustomUser
        depth = 1
        fields = (
            'id',
            'username',
            'email',
            'bio',
            'watched',
            'watchlist',
            'favorites',
            'recent'
        )


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8)
    email = serializers.EmailField(
                validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')   
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect username/password.')

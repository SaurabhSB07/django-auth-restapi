from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match")

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    email=serializers.CharField(max_length=255)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model=User
        fields= ["email","password"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["name","email"]
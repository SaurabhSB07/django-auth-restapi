from rest_framework import serializers
from .models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

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

class UserChangePasswordSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    user = self.context.get('user')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    user.set_password(password)
    user.save()
    return attrs

class UserChagePasswordResetEmailSerializer(serializers.Serializer):
   email=serializers.CharField(max_length=255)
   class Meta:
      fields=["email"]

def validate(self,attrs):
   if User.objects.filter(email=email).exists():
    user = User.objects.get(email = email)
    uid = urlsafe_base64_encode(force_bytes(user.id))
    print('Encoded UID', uid)
    token = PasswordResetTokenGenerator().make_token(user)
    print('Password Reset Token', token)
    link = 'http://localhost:3000/api/user/reset/'+uid+'/'+token
    print('Password Reset Link', link)
   

   return attrs
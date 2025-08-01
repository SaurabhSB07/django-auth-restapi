from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from .models import User


def get_tokens_for_user(user):
    if not user.is_active:
        raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'refresh': token['refresh'], 'access': token['access'], 'msg': 'Registration successful'})
        return Response(serializer.errors, status=400)


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'refresh': token['refresh'], 'access': token['access'], 'msg': 'Login successful'})
            else:
                return Response({"errors": {"non_field_errors": ["Email or password is incorrect"]}}, status=400)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=200)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Changed Successfully'}, status=200)


class UserChagePasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserChagePasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password reset link is sent to your email, kindly check your email"})


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset Successfully'}, status=200)




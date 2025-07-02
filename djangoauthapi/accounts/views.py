from rest_framework.response import Response  
from rest_framework.views import APIView
from .serializers import UserSerializer,UserLoginSerializer
from django.contrib.auth import authenticate


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Registration successful'})
        return Response(serializer.errors, status=400)
    
class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")

            user = authenticate(email=email, password=password)  
            if user is not None:
                return Response({'msg': 'Login successful'})
            else:
                return Response({
                    "errors": {"non_field_errors": ["Email or password is incorrect"]}
                }, status=400)

from rest_framework.response import Response  
from rest_framework.views import APIView
from .serializers import UserSerializer

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Registration successful'})
        return Response(serializer.errors, status=400)
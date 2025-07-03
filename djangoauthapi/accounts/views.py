from rest_framework.response import Response  
from rest_framework.views import APIView
from .serializers import UserSerializer,UserLoginSerializer,UserProfileSerializer
from django.contrib.auth import authenticate
from .rendrers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    from rest_framework_simplejwt.tokens import RefreshToken
    from rest_framework_simplejwt.exceptions import AuthenticationFailed

    if not user.is_active:
        raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg': 'Registration successful'})
        return Response(serializer.errors, status=400)
    
class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")

            user = authenticate(email=email, password=password)  
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'msg': 'Login successful','token':token})
            else:
                return Response({
                    "errors": {"non_field_errors": ["Email or password is incorrect"]}
                }, status=400)
            
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=200)      
 
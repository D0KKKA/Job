from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login, logout, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from users import models, serializers

User = get_user_model()
class UserView(viewsets.ModelViewSet):
    """
    Предоставляет CRUD-операции для пользователей.
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class RegistrationView(APIView):
    """
    Регистрирует нового пользователя.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=serializers.UserRegistrationSerializer,
        responses={status.HTTP_201_CREATED: "User registered successfully"}
    )
    def post(self, request):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "User registered successfully",
                "user": serializer.data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Авторизует пользователя.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=serializers.LoginSerializer,
        responses={status.HTTP_200_OK: "Authentication successful"}
    )
    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            refresh.payload.update({
                'user_id': user.id,
                'email': user.email
            })
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    """
    Выход пользователя из системы.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={status.HTTP_200_OK: "Logout successful"})
    def post(self, request):
        logout(request)
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token_type, refresh_token = auth_header.split(' ', 1)
            if token_type and refresh_token:
                try:
                    token = RefreshToken(refresh_token)
                    token.blacklist()
                except Exception as e:
                    return Response({'error': 'Invalid Refresh token'}, status=status.HTTP_400_BAD_REQUEST)
                return Response({'success': 'Logout successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Refresh token missing'}, status=status.HTTP_400_BAD_REQUEST)




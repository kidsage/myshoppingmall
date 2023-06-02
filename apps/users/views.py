from django.conf import settings
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet

from .error import EmailAlreadyExistsError
from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer, LoginSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    serializer_classes = {
        'login': LoginSerializer
    }

    def get_serializer_class(self):
        if hasattr(self, 'serializer_classes'):
            return self.serializer_classes.get(self.action, self.serializer_class)
        
        return super().get_serializer_class()

    def perform_create(self, serializer: UserSerializer):
        email = serializer.validated_data["email"]
        if User.objects.filter(email=email).exists():
            raise EmailAlreadyExistsError()

        User.objects.create_user(**serializer.validated_data)

    @action(detail=False, methods=["POST"])
    def login(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = User.objects.filter(email=email).first()
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if not user.check_password(password):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if not user.is_active:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return LoginResponse(user)


class LoginResponse(Response):
    def __init__(self, user: User):
        super().__init__(status=status.HTTP_200_OK)

        token = RefreshToken.for_user(user)

        refresh = str(token)
        access = str(token.access_token)

        self.set_cookie(
            key=settings.SIMPLE_JWT["AUTH_COOKIE"],
            value=access,
            max_age=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds(),
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
        )

        self.data = {
            "refresh": refresh,
            "access": access,
        }


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
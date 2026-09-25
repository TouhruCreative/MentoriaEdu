from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import RegisterSerializer, ProfileSerializer

from .models import User

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes= [AllowAny]

class ProfileView(APIView):

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
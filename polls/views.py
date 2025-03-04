from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Survey, Option, Vote
from .serializers import SurveySerializer, VoteSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions


User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Permitir a cualquiera registrarse

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados

    def get_object(self):
        return self.request.user  # Devuelve el usuario actual

class SurveyListCreateView(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class SurveyDetailView(generics.RetrieveAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]
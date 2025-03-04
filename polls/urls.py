from django.urls import path
from .views import UserCreateView, UserDetailView, SurveyListCreateView, SurveyDetailView, VoteCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register', UserCreateView.as_view(), name='user-register'),
    path('me', UserDetailView.as_view(), name='user-detail'),
    path('surveys', SurveyListCreateView.as_view(), name='survey-list'),
    path('surveys/<int:pk>', SurveyDetailView.as_view(), name='survey-detail'),
    path('surveys/<int:pk>/vote', VoteCreateView.as_view(), name='vote'),

    # Endpoints para obtener y refrescar el token
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
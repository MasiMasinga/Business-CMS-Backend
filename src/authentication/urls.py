from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, MyTokenObtainPairView, PasswordResetView, SetPasswordView

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', SetPasswordView.as_view(), name='password_reset_confirm'),
]

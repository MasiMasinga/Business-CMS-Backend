from django.urls import path
from .views import UpdateFirstNameView, UpdateEmailView, UpdatePasswordView

urlpatterns = [
    path('update-name/<int:pk>/', UpdateFirstNameView.as_view(), name='update-first-name'),
    path('update-email/<int:pk>/', UpdateEmailView.as_view(), name='update-email'),
    path('update-password/<int:pk>/', UpdatePasswordView.as_view(), name='update-password'),
]
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UpdateFirstNameSerializer, UpdateEmailSerializer, UpdatePasswordSerializer

User = get_user_model()

class UpdateFirstNameView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateFirstNameSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user.first_name = serializer.validated_data.get('first_name')
            user.save()
            return Response({"message": "First name updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateEmailView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateEmailSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            new_email = serializer.validated_data.get('new_email')
            user.email = new_email
            user.save()
            return Response({"message": "Email updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdatePasswordSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            new_password = serializer.validated_data.get('new_password')
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'last_name': {'required': False},
        }

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        self.reset_form = PasswordResetForm(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError('Invalid email.')
        return value

    def save(self):
        request = self.context.get('request')
        self.reset_form.save(use_https=request.is_secure(), request=request)


class SetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    uid = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        try:
            uid = urlsafe_base64_decode(attrs.get('uid')).decode()
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            raise serializers.ValidationError({'uid': ['Invalid value']})

        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({"message": "Passwords do not match."})

        data = {
            'new_password1': password,
            'new_password2': confirm_password,
            'token': attrs.get('token'),
            'uid': attrs.get('uid'),
        }

        self.set_password_form = SetPasswordForm(user=user, data=data)

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs
    
    def save(self):
        return self.set_password_form.save()
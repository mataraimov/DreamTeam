from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Account


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token


class AccountSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )
    username = serializers.CharField(
        write_only=True,
        required=True,
    )
    first_name = serializers.CharField(
        write_only=True,
        required=True,
    )
    last_name = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password', 'password2', 'phone_number', 'first_name', 'last_name']


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


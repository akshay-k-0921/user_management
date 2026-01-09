from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # create empty profile
        Profile.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        from django.contrib.auth import authenticate

        identifier = data.get("identifier")
        password = data.get("password")

        user = authenticate(username=identifier, password=password)

        if not user:
            try:
                user_obj = User.objects.get(email__iexact=identifier)
                user = authenticate(
                    username=user_obj.username,
                    password=password
                )
            except User.DoesNotExist:
                pass

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data["user"] = user
        return data


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    dob = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = Profile
        fields = [
            "username",
            "full_name",
            "dob",
            "address",
            "gender",
            "mobile_number",
            "email",
        ]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")

        validate_password(data["new_password"])
        return data

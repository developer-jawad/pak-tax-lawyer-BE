from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

User = get_user_model()


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "is_active",
        ]
        read_only_fields = ["id"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        full_name = f"{instance.first_name} {instance.last_name}".strip()
        representation["name"] = full_name
        return representation


class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=255, required=True)
    password2 = None
    username = None

    def validate_email(self, email):
        """
        Check if a user with this email already exists.
        """
        email = self.normalize_email(email)
        try:
            existing_user = User.objects.get(email__iexact=email)
            if not existing_user.is_active:
                raise serializers.ValidationError(
                    _(
                        "An account with this email address exists but is currently inactive. Please contact the administrator for assistance."
                    )
                )
            else:
                raise serializers.ValidationError(
                    _(
                        "We are unable to create an account with this email address. Please contact the administrator for assistance."
                    )
                )
        except User.DoesNotExist:
            pass
        return email

    def normalize_email(self, email):
        """Normalize the email address"""
        return email and email.lower() or ""

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["name"] = self.validated_data.get("name", "")
        return data

    def validate(self, data):
        """
        Override parent validation to skip password2 confirmation check.

        Since this serializer sets password2 = None to disable password confirmation,
        we need to override the default validation that expects both password1 and password2
        to be present and match.
        """
        return data

    def save(self, request):
        user = super().save(request)
        full_name = self.validated_data.get("name", "")
        name_parts = full_name.split(maxsplit=1)
        user.first_name = name_parts[0]
        user.last_name = name_parts[1] if len(name_parts) > 1 else ""
        user.save()
        return user


class CustomLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            # First check if user exists and is active
            try:
                user = User.objects.get(email__iexact=email)
                if not user.is_active:
                    raise serializers.ValidationError(
                        _(
                            "Your account is currently inactive. Please contact the administrator for assistance."
                        )
                    )
            except User.DoesNotExist:
                # Let the parent class handle the "invalid credentials" message
                pass

        # Call parent validation
        return super().validate(attrs)

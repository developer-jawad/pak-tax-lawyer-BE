from rest_framework import serializers

from home.models import HeroSection


class HeroSectionSerializer(serializers.ModelSerializer):
    background_image = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model = HeroSection
        fields = [
            'id',
            'title',
            'subtitle',
            'description',
            'button_text',
            'button_link',
            'background_gradient',
            'background_image_url',
            'background_image',
            'created_at',
            'updated_at',
            'is_active',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate(self, data):
        if not data.get('background_image') and not data.get('background_image_url'):
            raise serializers.ValidationError(
                "Either background_image or background_image_url must be provided."
            )
        return data
    
    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value.strip()
    
    def validate_subtitle(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Subtitle cannot be empty.")
        return value.strip()
    
    def validate_description(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Description cannot be empty.")
        return value.strip()
    
    def validate_button_text(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Button text cannot be empty.")
        return value.strip()

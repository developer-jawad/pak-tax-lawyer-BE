from common.api.serializers import DynamicFieldsModelSerializer

from home.models import TestimonialCTA


class TestimonialCTASerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TestimonialCTA
        fields = [
            'id',
            'title',
            'description',
            'button_text',
            'button_link',
            'is_testimonial_section',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

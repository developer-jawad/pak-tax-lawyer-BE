from common.api.serializers import DynamicFieldsModelSerializer

from videos.models import VideoSection


class VideoSectionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = VideoSection
        fields = [
            'id',
            'title',
            'subtitle',
            'description',
            'search_placeholder',
            'no_results',
            'try_adjusting',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

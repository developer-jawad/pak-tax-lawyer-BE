from common.api.serializers import DynamicFieldsModelSerializer

from videos.models import VideoHero


class VideoHeroSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = VideoHero
        fields = [
            'id',
            'title',
            'subtitle',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

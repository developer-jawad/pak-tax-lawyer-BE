from common.api.serializers import DynamicFieldsModelSerializer

from videos.models import VideoStatistic


class VideoStatisticSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = VideoStatistic
        fields = [
            'id',
            'number',
            'label',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

from rest_framework import serializers
from .video_statistic import VideoStatisticSerializer
from .video_hero import VideoHeroSerializer
from .video import VideoSerializer
from .video_section import VideoSectionSerializer
from .video_cta import VideoCTASerializer

__all__ = [
    'VideoStatisticSerializer',
    'VideoHeroSerializer',
    'VideoSerializer',
    'VideoSectionSerializer',
    'VideoCTASerializer',
]
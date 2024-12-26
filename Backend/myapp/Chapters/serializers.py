from rest_framework.serializers import ModelSerializer
from .models import Chapters

class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapters
        fields = "__all__"
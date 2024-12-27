from rest_framework.serializers import ModelSerializer
from .models import Topics

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topics
        fields = "__all__"
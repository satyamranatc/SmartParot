from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Topics
from .serializers import TopicSerializer

@api_view(["GET", "POST"])
def getTopics(requests):
    if requests.method == "GET":
        allTopics = Topics.objects.all()
        allTopicsData = TopicSerializer(allTopics,many=True)
        return Response(allTopicsData.data)
    
    elif requests.method == "POST":
        newTopic = TopicSerializer(data=requests.data)
        if newTopic.is_valid():
            newTopic.save()
            return Response(newTopic.data, status=201)
        
        return Response(newTopic.errors, status=400)
    
    return Response('Invalid Method')
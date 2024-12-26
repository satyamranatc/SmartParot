from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Chapters
from .serializers import ChapterSerializer

@api_view(["GET", "POST"])
def getChapters(requests):
    
    if requests.method == "GET":
        
        allChapters = Chapters.objects.all()
        allChaptersData = ChapterSerializer(allChapters,many=True)
        return Response(allChaptersData.data)
    
    elif requests.method == "POST":
        
        newChapter = ChapterSerializer(data=requests.data)
        if newChapter.is_valid():
            newChapter.save()
            return Response(newChapter.data, status=201)
        
        return Response(newChapter.errors, status=400)
    
    return Response('Invalid Method')
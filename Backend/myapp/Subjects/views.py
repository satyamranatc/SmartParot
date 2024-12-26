from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Subjects
from .serializers import SubjectSerializer

@api_view(["GET"])
def Subjects(requests):
    allSubjects = Subjects.objects.all()
    allSubjectsData = SubjectSerializer(allSubjects,many=True)
    return Response(allSubjectsData.data)


@api_view(["POST"])
def Subjects(requests):
    newSubject = SubjectSerializer(data=requests.data)
    if newSubject.is_valid():
        newSubject.save()
        return Response(newSubject.data, status=201)
    else:
        return Response(newSubject.errors, status=400)
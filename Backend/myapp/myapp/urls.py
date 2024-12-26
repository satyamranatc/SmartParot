from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('/api/Subjects', include('Subjects')),
    path('/api/topics', include('Topics')),
    path('/api/chapters', include('Chapters')),
    path('admin/', admin.site.urls),
]

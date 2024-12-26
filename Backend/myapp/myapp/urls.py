from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/subjects', include('Subjects.urls')),
    path('api/topics', include('Topics.urls')),
    path('api/chapters', include('Chapters.urls')),
    path('admin/', admin.site.urls),
]

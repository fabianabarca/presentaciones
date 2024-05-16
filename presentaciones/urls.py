from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('demo/', include('demo.urls')),
    path('cursos/', include('courses.urls')),
    path('estudiantes/', include('users.urls')),
    path('presentaciones/', include('decks.urls')),
]

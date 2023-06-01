from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('cursos/', include('courses.urls')),
    path('usuarios/', include('users.urls'), name='usuarios'),
]

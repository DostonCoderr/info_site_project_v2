from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

# добавляем это для загрузки файлов в режиме разработки
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

urlpatterns = [
    path('bobur/', admin.site.urls),
    path('', include('pages.urls')),  
    re_path(r'^google9f3904655a724430\.html$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),# твое приложение
]

# разрешаем отдачу медиафайлов при DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

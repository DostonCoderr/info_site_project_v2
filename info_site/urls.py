from django.contrib import admin
from django.urls import path, include

# добавляем это для загрузки файлов в режиме разработки
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # твое приложение
]

# разрешаем отдачу медиафайлов при DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

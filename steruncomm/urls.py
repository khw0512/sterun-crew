from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path('users/', include('users.urls')),
    path("attendance/", include("attendance.urls")),
    path("runres/", include("record.urls")),
    path("bingo/", include("bingo.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
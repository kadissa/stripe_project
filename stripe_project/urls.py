from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    ]

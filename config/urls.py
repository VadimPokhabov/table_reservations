from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('reservation.urls', namespace='reservation')),
    path('users/', include('users.urls'), name='users'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS))

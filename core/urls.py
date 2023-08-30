
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


# url patterns link into system
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home_page, name='home'),
    path('taskmanagement/',views.taskmanagement,name = 'taskmanagement'),
    path('auth/', include('apps.account.urls', namespace='account')),
    path('team/', include('apps.team.urls', namespace='team')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

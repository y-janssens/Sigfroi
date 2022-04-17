from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('fiches/', include('fiches.urls')),
    path('reputations/', include('reputations.urls')),
    path('api/', include('api.urls')),
    path('auth/', include('base.urls')),
    path('carrieres/', include('carrieres.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'backend.views.view_404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

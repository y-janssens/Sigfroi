from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.timeline, name="timeline"),
    path('iframe', views.timeline_iframe, name="timeline_iframe"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.timeline, name="timeline"),
    path('iframe', views.timeline_iframe, name="timeline_iframe"),
    #path('app', TemplateView.as_view(template_name='index.html'), name="app")
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.avatars, name="avatars"),
    path('iframe', views.avatars_iframe, name="avatars_iframe"),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.reals, name="reals"),
    path('blason/', views.shield, name="shield"),
    path('herse/', views.gates, name="gates"),
    path('remparts/', views.walls, name="walls"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

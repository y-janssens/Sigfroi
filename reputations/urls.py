from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('edit/<int:pk>', views.editReputation, name="edit-reputation")
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

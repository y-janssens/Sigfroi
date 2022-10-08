from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('edit/<str:pk>', views.editReputation, name="edit-reputation"),
    path('details/<str:pk>', views.reputationsDetails, name="reputations_details"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

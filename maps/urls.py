from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.maps, name="maps"),
    path('add', views.add_map, name="add_map"),
    path('confirm/<str:pk>', views.confirm_map, name="confirm_map"),
    path('delete/<str:pk>', views.delete_map, name="delete_map"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

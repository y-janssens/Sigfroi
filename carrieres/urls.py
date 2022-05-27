from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.carrieres, name="carrieres"),
    path('<str:pk>', views.carriere, name="carriere"),
    path('details/', views.carrieresDetails, name="carrieres_details"),
    path('add/', views.addCarriere, name="add_carriere"),
    path('edit/<str:pk>', views.editCarriere, name="edit_carriere"),
    path('delete/<str:pk>', views.deleteCarriere, name="delete_carriere"),
    path('confirm/<str:pk>', views.confirmCarriere, name="confirm_carriere"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
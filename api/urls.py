from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('', views.getRoutes, name="api_routes"),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('carrieres/add/', views.createCarriere, name="carrieres_add_api"),
    path('carrieres/', views.carrieresRoutes, name="carrieres_api"),
    path('carrieres/<str:pk>/', views.carriereRoute, name="carriere_id_api"),

    path('fiches/add/', views.createFiche, name="fiches_add_api"),
    path('fiches/', views.fichesRoutes, name="fiches_api"),
    path('fiches/<str:pk>/', views.ficheRoute, name="fiche_id_api"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

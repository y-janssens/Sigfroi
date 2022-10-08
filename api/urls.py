from django.urls import path
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

    path('carrieres/', views.carrieresRoutes, name="carrieres_api"),
    path('carrieres/add/', views.createCarriere, name="carrieres_add_api"),
    path('carrieres/edit/<str:pk>/',
         views.editCarriereRoute, name="carrieres_edit_api"),
    path('carrieres/<str:pk>/', views.carriereRoute, name="carriere_id_api"),

    path('fiches/', views.fichesRoutes, name="fiches_api"),
    path('fiches/add/', views.createFiche, name="fiches_add_api"),
    path('fiches/edit/<str:pk>/', views.editFicheRoute, name="fiches_edit_api"),
    path('fiches/<str:pk>/', views.ficheRoute, name="fiche_id_api"),

    path('flavor/', views.reputationsTextRoute, name="flavor_text"),
    path('reputations/<str:pk>/', views.reputationRoute, name="reputation_id_api"),
    path('reputations/edit/<str:pk>/',
         views.editReputationRoute, name="reputation_edit_api"),

    path('competences/', views.competencesRoutes, name="competences_api"),
    path('competences/<str:pk>/', views.competenceRoute, name="competence_id_api"),

    path('equipement/armes/', views.weaponsRoutes, name="weapons_api"),
    path('equipement/armes/<str:pk>/', views.weaponRoute, name="weapon_id_api"),

    path('equipement/armures/', views.armorsRoutes, name="armors_api"),
    path('equipement/armures/<str:pk>/', views.armorRoute, name="armor_id_api"),

    path('timeline/', views.timelineRoutes, name="timeline_api"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

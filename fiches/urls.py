from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.fiches, name="index"),
    path('fiche/<str:pk>', views.fiche, name="charsheet"),
    path('fiche/details/<str:pk>', views.ficheDetails, name="charsheet_details"),
    path('fiche/model/<str:pk>', views.ficheModel, name="charsheet_model"),
    path('fiche/model/iframe/<str:pk>', views.ficheModelIframe,
         name="charsheet_model_iframe"),
    path('add', views.addFiche, name="add_fiche"),
    path('delete/<str:pk>', views.delFiche, name="delete_fiche"),
    path('confirm/<str:pk>', views.confirmFiche, name="confirm_fiche"),
    path('edit/<str:pk>', views.editFiche, name="edit"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.fiches, {'results': True}, name="index"),
    path('inactifs', views.fiches, {'results': False}, name="index_inactives"),
    path('fiche/<int:pk>', views.fiche, name="charsheet"),
    path('fiche/details/<int:pk>', views.ficheDetails, name="charsheet_details"),
    path('fiche/model/<int:pk>', views.ficheModel, name="charsheet_model"),
    path('fiche/model/iframe/<int:pk>', views.ficheModelIframe,
         name="charsheet_model_iframe"),
    path('add', views.addFiche, name="add_fiche"),
    path('delete/<int:pk>', views.delFiche, name="delete_fiche"),
    path('confirm/<int:pk>', views.confirmFiche, name="confirm_fiche"),
    path('edit/<int:pk>', views.editFiche, name="edit"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

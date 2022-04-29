from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.competences, name="competences"),
    path('<str:pk>', views.competence, name="competence"),
    path('add/', views.addCompetence, name="add_competence"),
    path('edit/<str:pk>', views.editCompetence, name="edit_competence"),
    path('delete/<str:pk>', views.deleteCompetence, name="delete_competence"),
    path('confirm/<str:pk>', views.confirmCompetence, name="confirm_competence"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
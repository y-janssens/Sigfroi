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

    path('addSheet/<str:pk>', views.addSkillSheet, name="add_skillSheet"),
    path('editSkill/<str:pk>', views.editSkillSheet, name="edit_skillSheet"),
    path('confirmSheet/<str:pk>', views.confirmSkillSheet,
         name="confirm_skillSheet"),
    path('deleteSheet/<str:pk>', views.deleteSkillSheet, name="delete_skillSheet"),

    path('iframe/', views.SkillSheetIframe, name="iframe_skillSheet_list"),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

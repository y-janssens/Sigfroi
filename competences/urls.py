from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.competences, name="competences"),
    path('<int:pk>', views.competence, name="competence"),
    path('add/', views.addCompetence, name="add_competence"),
    path('edit/<int:pk>', views.editCompetence, name="edit_competence"),
    path('delete/<int:pk>', views.deleteCompetence, name="delete_competence"),
    path('confirm/<int:pk>', views.confirmCompetence, name="confirm_competence"),

    path('addSheet/<int:pk>', views.addSkillSheet, name="add_skillSheet"),
    path('editSkill/<int:pk>', views.editSkillSheet, name="edit_skillSheet"),
    path('confirmSheet/<int:pk>', views.confirmSkillSheet,
         name="confirm_skillSheet"),
    path('deleteSheet/<int:pk>', views.deleteSkillSheet, name="delete_skillSheet"),

    path('iframe/', views.SkillSheetIframe, name="iframe_skillSheet_list"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

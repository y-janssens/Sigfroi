from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.achievements, name="achievements"),
    path('<str:pk>', views.achievement, name="achievement"),
    path('<str:pk>/edit', views.editAchievement, name="edit_achievement"),
    path('edit/<str:pk>', views.editPlayerAchievement, name="edit_achievements"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('armes/', views.weapons, name="weapons"),
    path('armures/', views.armors, name="armors"),
    #path('<str:pk>', views.competence, name="equipement"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
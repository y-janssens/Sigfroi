from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.fiches, name="index"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('fiches/<str:pk>', views.fiche, name="charsheet"),
    path('fiches/details/<str:pk>', views.ficheDetails, name="charsheet_details"),
    path('add', views.addFiche, name="add_fiche"),
    path('delete/<str:pk>', views.delFiche, name="delete_fiche"),
    path('confirm/<str:pk>', views.confirm, name="confirm"),
    path('edit/<str:pk>', views.editFiche, name="edit"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
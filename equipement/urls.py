from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('armes/', views.weapons, name="weapons"),
    path('armes/<str:pk>/', views.weapon, name="weapon"), 
    path('add/weapon', views.addWeapon, name="add_weapon"),
    path('armes/edit/<str:pk>', views.editWeapon, name="edit_weapon"),
    path('armes/delete/<str:pk>', views.deleteWeapon, name="delete_weapon"),
    path('armes/confirm/<str:pk>', views.confirmWeapon, name="confirm_weapon"),

    path('armures/', views.armors, name="armors"),
    path('armures/<str:pk>/', views.armor, name="armor"),
    path('add/armure', views.addArmor, name="add_armor"),
    path('armures/edit/<str:pk>', views.editArmor, name="edit_armor"),
    path('armures/delete/<str:pk>', views.deleteArmor, name="delete_armor"),
    path('armures/confirm/<str:pk>', views.confirmArmor, name="confirm_armor"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

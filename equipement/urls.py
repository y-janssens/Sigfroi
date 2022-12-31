from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('armurerie/', views.armory, name="armory"),
    path('armurerie/iframe/', views.armoryIframe, name="armory_iframe"),
    path('armes/', views.weapons, name="weapons"),
    path('armes/<int:pk>/', views.weapon, name="weapon"),
    path('add/weapon', views.addWeapon, name="add_weapon"),
    path('armes/edit/<int:pk>', views.editWeapon, name="edit_weapon"),
    path('armes/delete/<int:pk>', views.deleteWeapon, name="delete_weapon"),
    path('armes/confirm/<int:pk>', views.confirmWeapon, name="confirm_weapon"),

    path('armures/', views.armors, name="armors"),
    path('armures/<int:pk>/', views.armor, name="armor"),
    path('add/armure', views.addArmor, name="add_armor"),
    path('armures/edit/<int:pk>', views.editArmor, name="edit_armor"),
    path('armures/delete/<int:pk>', views.deleteArmor, name="delete_armor"),
    path('armures/confirm/<int:pk>', views.confirmArmor, name="confirm_armor"),

    path('addSheet/<int:pk>', views.addStuffSheet, name="add_stuffSheet"),
    path('confirmSheet/<int:pk>', views.confirmStuffSheet,
         name="confirm_stuffSheet"),
    path('deleteSheet/<int:pk>', views.deleteStuffSheet, name="delete_stuffSheet"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

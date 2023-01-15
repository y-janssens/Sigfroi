from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('characters/', views.characters, name="characters"),
    path('characters/add', views.add_characters, name="add_characters"),
    path('characters/confirm/<str:pk>', views.confirm_character, name="confirm_character"),
    path('characters/delete/<str:pk>', views.delete_character, name="delete_character"),

    path('trees/', views.family_trees, name="family_trees"),
    path('trees/add', views.add_family_tree, name="add_family_tree"),
    path('trees/confirm/<str:pk>', views.confirm_tree, name="confirm_tree"),
    path('trees/delete/<str:pk>', views.delete_tree, name="delete_tree"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

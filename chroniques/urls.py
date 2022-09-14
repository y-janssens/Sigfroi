from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.chroniques, name="chroniques"),
    path('<str:pk>/', views.chronique, name="chronique"),
    path('new', views.newChronique, name="new_chronique"),
    path('add', views.addChronique, name="add_chronique"),
    path('confirm/<str:pk>', views.confirmChronique, name="confirm_chronique"),
    path('delete/<str:pk>/', views.deleteChronique, name="delete_chronique"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

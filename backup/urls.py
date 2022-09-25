from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.backups, name="backups"),
    path('add/', views.backup, name="backup"),
    path('confirmSnapshot/<uuid:slug>',
         views.confirmSnapshot, name="confirm_snapshot"),
    path('delete/<uuid:slug>', views.delBackup, name="delete_backup"),
    path('send/<uuid:slug>', views.sendBackup, name="send_backup"),
    path('restore/<uuid:slug>', views.restore, name="restore_backup"),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

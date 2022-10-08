from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.backups, name="backups"),
    path('add/', views.backup, name="backup"),
    path('confirmSnapshot/<uuid:slug>',
         views.confirmSnapshot, name="confirm_snapshot"),
    path('delete/<uuid:slug>', views.delBackup, name="delete_backup"),
    path('restore/<uuid:slug>', views.restore, name="restore_backup"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

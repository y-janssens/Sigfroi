from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/', include('api.urls')),
    path('', include('fiches.urls')),
    path('reputations/', include('reputations.urls')),
    path('competences/', include('competences.urls')),
    path('equipements/', include('equipement.urls')),
    path('user/', include('users.urls')),
    path('carrieres/', include('carrieres.urls')),
    path('listing/', include('listing.urls')),
    path('cartes/', include('cartes.urls')),
    path('succes/', include('succes.urls')),
    path('reals/', include('realtime.urls')),
    path('timeline/', include('timeline.urls')),
    path('battle/', include('combat.urls')),
    path('backups/', include('backup.urls')),
    path('chronicles/', include('chroniques.urls')),
    path('avatars/', include('avatars.urls')),
    path('tools/', include('tools.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'backend.views.view_404'


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

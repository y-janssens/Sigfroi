from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #path('', views.home, name="home"),
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
    path('battle/', include('combat.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'backend.views.view_404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

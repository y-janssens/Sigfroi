from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
#from django.views.generic import TemplateView
=======
>>>>>>> 2351af928aae08e2d5ac1c50cac3815b9ea03ce9
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('fiches/', include('fiches.urls')),
<<<<<<< HEAD
    #path('react/', TemplateView.as_view(template_name='index.html')),
=======
    path('reputations/', include('reputations.urls')),
>>>>>>> 2351af928aae08e2d5ac1c50cac3815b9ea03ce9
    #path('api/', include('api.urls')),
    path('auth/', include('base.urls')),
    path('carrieres/', include('carrieres.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'backend.views.view_404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

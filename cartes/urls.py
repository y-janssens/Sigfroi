from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.cards, name="cards"),
    path('addSheet/<str:pk>', views.addCardSheet, name="add_cardSheet"),
    path('confirmSheet/<str:pk>', views.confirmCardSheet, name="confirm_cardSheet"),
    path('deleteSheet/<str:pk>', views.deleteCardSheet, name="delete_cardSheet"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

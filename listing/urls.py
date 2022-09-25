from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.listing, name="listing"),

    path('addSheet/<str:pk>', views.addAliasSheet, name="add_aliasSheet"),
    path('confirmSheet/<str:pk>/<str:slug>',
         views.confirmAliasSheet, name="confirm_aliasSheet"),
    path('deleteSheet/<str:pk>/<str:slug>',
         views.deleteAliasSheet, name="delete_aliasSheet"),

    path('iframe/', views.listingIframe, name="listing_iframe"),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

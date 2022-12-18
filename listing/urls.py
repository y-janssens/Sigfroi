from django.urls import path
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

    path('pantheon/', views.pantheon, name="pantheon"),
    path('pantheon/iframe/', views.pantheon_iframe, name="pantheon_iframe"),
    path('pantheon/add/', views.addFinisher, name="add_finisher"),
    path('pantheon/confirm/<str:pk>', views.confirmFinisher, name="confirm_finisher"),
    path('pantheon/delete/<str:pk>', views.deleteFinisher, name="delete_finisher"),

    path('pantheon/custom/confirm/<str:pk>', views.confirmCustom, name="confirm_custom"),
    path('pantheon/custom/delete/<str:pk>', views.deleteCustom, name="delete_custom")
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

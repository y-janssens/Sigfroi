from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.chroniques, name="chroniques"),
    path('<int:pk>/', views.chronique, name="chronique"),
    path('new', views.newChronique, name="new_chronique"),
    path('add', views.addChronique, name="add_chronique"),
    path('confirm/<int:pk>', views.confirmChronique, name="confirm_chronique"),
    path('delete/<int:pk>/', views.deleteChronique, name="delete_chronique"),

    path('monthly', views.news_chroniques, name="news_chroniques"),
    path('monthly/new', views.newNewsChronique, name="new_news_chronique"),
    path('monthly/add', views.addNewsChronique, name="add_news_chronique"),
    path('monthly/<int:pk>/', views.news_chronique, name="news_chronique"),
    path('monthly/<int:pk>/iframe', views.news_chronique_iframe, name="news_chronique_iframe"),
    path('monthly/edit/<int:pk>/', views.edit_news_chronique, name="edit_news_chronique"),
    path('monthly/confirm/<int:pk>', views.confirm_News_Chronique, name="confirm_news_chronique"),
    path('monthly/delete/<int:pk>/', views.deleteNewsChronique, name="delete_news_chronique"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('bars/', views.progress_bars, name="progress_bars"),
    path('bars/iframe/<int:pk>', views.progress_bar_iframe, name="progress_bar_iframe"),
    path('bars/add', views.add_progress_bar, name="add_progress_bar"),
    path('bars/edit/<int:pk>', views.edit_progress_bar, name="edit_progress_bar"),
    path('bars/confirm/<int:pk>', views.confirm_progress_bar, name="confirm_progress_bar"),
    path('bars/delete/<int:pk>', views.delete_progress_bar, name="delete_progress_bar"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

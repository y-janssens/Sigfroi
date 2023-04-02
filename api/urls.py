from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import TimelineViewSet, LineageViewSet
from .backups.views import BackupViewSet
from .stuff.views import StuffSheetViewSet, ArmorsViewSet, WeaponsViewSet
from .skills.views import SkillSheetsViewSet, SkillsViewSet
from .achivements.views import AchievementsSheetsViewSet
from .cards.views import CardSheetViewSet
from .sheets.views import SheetsViewSet, PathViewSet, ListingViewSet, ReputationViewSet
from .maps.views import MapViewSet, ItemsViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'fiches', SheetsViewSet)
router.register(r'skills_list', SkillsViewSet)
router.register(r'armors', ArmorsViewSet)
router.register(r'weapons', WeaponsViewSet)
router.register(r'carrieres', PathViewSet)
router.register(r'timeline', TimelineViewSet)
router.register(r'listing', ListingViewSet)
router.register(r'backups', BackupViewSet)
router.register(r'lineage', LineageViewSet)
router.register(r'maps', MapViewSet)
router.register(r'items', ItemsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('stuff/<int:owner_id>/', StuffSheetViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('stuff/<int:owner_id>/<int:pk>/', StuffSheetViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
    path('skills/<int:owner_id>/', SkillSheetsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('skills/<int:owner_id>/<int:pk>/', SkillSheetsViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
    path('cards/<int:owner_id>/', CardSheetViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cards/<int:owner_id>/<int:pk>/', CardSheetViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
    path('reputations/<int:owner_id>/', ReputationViewSet.as_view({'get': 'list', 'patch': 'partial_update'})),
    path('achievements/<int:owner_id>/', AchievementsSheetsViewSet.as_view({'get': 'list', 'patch': 'partial_update'}))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

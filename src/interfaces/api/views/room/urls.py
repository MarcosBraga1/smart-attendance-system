from rest_framework.routers import DefaultRouter
from .room_view import RoomViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet, basename='room')

urlpatterns = router.urls
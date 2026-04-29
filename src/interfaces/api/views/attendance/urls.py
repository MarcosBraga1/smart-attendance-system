from rest_framework.routers import DefaultRouter
from .attendance_view import AttendanceViewSet

router = DefaultRouter()
router.register(r'attendances', AttendanceViewSet, basename='attendance')

urlpatterns = router.urls
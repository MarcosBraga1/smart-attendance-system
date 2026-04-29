from rest_framework.routers import DefaultRouter
from .class_session_view import ClassSessionViewSet

router = DefaultRouter()
router.register(r'class_sessions', ClassSessionViewSet, basename='class_session')

urlpatterns = router.urls
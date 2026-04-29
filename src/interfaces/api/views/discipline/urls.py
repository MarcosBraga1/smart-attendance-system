from rest_framework.routers import DefaultRouter
from .discipline_view import DisciplineViewSet

router = DefaultRouter()
router.register(r'disciplines', DisciplineViewSet, basename='discipline')

urlpatterns = router.urls
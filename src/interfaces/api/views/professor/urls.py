from rest_framework.routers import DefaultRouter
from .professor_views import ProfessorViewSet

router = DefaultRouter()
router.register(r'professors', ProfessorViewSet, basename='professor')

urlpatterns = router.urls
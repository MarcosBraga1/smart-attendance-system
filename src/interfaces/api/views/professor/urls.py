from rest_framework.routers import DefaultRouter
from .professor_view import ProfessorViewSet

router = DefaultRouter()
router.register(r'professors', ProfessorViewSet, basename='professor')

urlpatterns = router.urls
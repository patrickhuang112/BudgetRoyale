from budgetroyale.models import BudgetSubmission
from django.conf.urls import url
from rest_framework import routers
from .views import BudgetSubmissionViewSet, RoomViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'users', UserViewSet)
router.register(r'budgetsubmissions', BudgetSubmissionViewSet)

urlpatterns = router.urls
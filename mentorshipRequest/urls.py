from django.urls import path, include
from rest_framework import routers

from .views import MenteeViewSet, MenteeDepartmentViewSet, MenteeDesignationViewSet, MenteeDisciplineViewSet, \
    MenteeEducationViewSet, MenteeResearchViewSet, mentoringRequestViewSet

router = routers.DefaultRouter()
router.register('mentoringRequest', mentoringRequestViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

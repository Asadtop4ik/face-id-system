from django.urls import path, include
from employees.views import FaceViewSet, AttendanceViewSet, CustomTokenObtainPairView, ProfileUserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'faces', FaceViewSet, basename='face')
router.register(r'attendances', AttendanceViewSet, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
]



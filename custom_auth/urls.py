from django.urls import path
from .views import CustomTokenObtainPairView, ProfileUserView


urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
]
from django.urls import path
from .views import CustomUserCreate
from .views import LoginView

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

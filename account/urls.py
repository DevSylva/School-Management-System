from django.urls import path
from .views import RegisterView
from .views import AllUsersView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('all-users/', AllUsersView.as_view(), name=('allUsers')),
]

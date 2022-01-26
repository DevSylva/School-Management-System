from django.urls import path
from .views import StudentProfileView

urlpatterns = [
    path('student-profile-update/', StudentProfileView.as_view(), name='studentProfileUpdate'),
]

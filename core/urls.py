from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, 
    LoginView,
    PatientViewSet,
    DoctorViewSet,
    PatientDoctorMappingViewSet
    )

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'doctors', DoctorViewSet)
router.register(r'mappings', PatientDoctorMappingViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
    path('',  include(router.urls)),
]
from django.urls import path, include
from rest_framework import routers
from . import views
from . import api_views

app_name = 'core'

# DRF router for API
router = routers.DefaultRouter()
router.register('patients', api_views.PatientViewSet)
router.register('doctors', api_views.DoctorViewSet)
router.register('appointments', api_views.AppointmentViewSet)
router.register('records', api_views.MedicalRecordViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients_list, name='patients_list'),
    path('appointments/', views.appointments_list, name='appointments_list'),
    path('appointments/new/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/edit/', views.appointment_edit, name='appointment_edit'),

    # API
    path('api/', include((router.urls, 'api'))),
]


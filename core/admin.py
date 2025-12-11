from django.contrib import admin
from .models import Patient, Doctor, Appointment, MedicalRecord

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','phone','created_at')
    search_fields = ('full_name','email','phone')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name','specialization','email','available')
    search_fields = ('full_name','specialization')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient','doctor','date','time','status')
    list_filter = ('status','date')
    search_fields = ('patient__full_name','doctor__full_name')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient','doctor','visit_date')
    search_fields = ('patient__full_name','doctor__full_name')


# Register your models here.

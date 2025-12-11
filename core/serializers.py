from rest_framework import serializers
from .models import Patient, Doctor, Appointment, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ('created_at',)

    def validate(self, data):
        # simple example: future date check
        from django.utils import timezone
        appointment_date = data.get('date')
        if appointment_date and appointment_date < timezone.localdate():
            raise serializers.ValidationError("Appointment date must be today or in the future.")
        return data

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        read_only_fields = ('created_at',)

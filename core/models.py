from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

GENDER_CHOICES = (('M','Male'),('F','Female'),('O','Other'))

class Patient(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    full_name = models.CharField(max_length=200)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    full_name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.specialization})"

class Appointment(models.Model):
    STATUS = (('P','Pending'),('A','Approved'),('C','Cancelled'),('F','Finished'))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='P')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('doctor', 'date', 'time')  # simple conflict avoidance
        ordering = ['-date', '-time']

    def __str__(self):
        return f"Appt: {self.patient} with {self.doctor} on {self.date} {self.time}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    visit_date = models.DateField(default=timezone.now)
    notes = models.TextField()
    prescriptions = models.TextField(blank=True)
    attachments = models.FileField(upload_to='records/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-visit_date']

    def __str__(self):
        return f"Record {self.patient} @ {self.visit_date}"


# Create your models here.

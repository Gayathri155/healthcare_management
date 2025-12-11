from django import forms
from .models import Appointment, Patient, MedicalRecord

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient','doctor','date','time','reason','status']
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'time': forms.TimeInput(attrs={'type':'time'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['full_name','dob','gender','phone','email','address']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient','doctor','visit_date','notes','prescriptions','attachments']
        widgets = {'visit_date': forms.DateInput(attrs={'type':'date'})}



from django import forms
from .models import Appointment, Patient, MedicalRecord

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor, Appointment, MedicalRecord
from .forms import AppointmentForm, PatientForm, MedicalRecordForm

# -----------------------------
# Home page
# -----------------------------
def home(request):
    return render(request, 'core/home.html')


# -----------------------------
# Patients list
# -----------------------------
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'core/patients_list.html', {'patients': patients})


# -----------------------------
# Appointments list
# -----------------------------
def appointments_list(request):
    appointments = Appointment.objects.select_related('patient', 'doctor').all()
    return render(request, 'core/appointments_list.html', {'appointments': appointments})


# -----------------------------
# Create a new appointment
# -----------------------------
@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save to database
            return redirect('core:appointments_list')
        else:
            print(form.errors)  # DEBUG: print form errors to console
    else:
        form = AppointmentForm()

    return render(request, 'core/appointment_form.html', {
        'form': form,
        'form_title': 'Create New Appointment'
    })


# -----------------------------
# Edit an existing appointment
# -----------------------------
@login_required
def appointment_edit(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appt)
        if form.is_valid():
            form.save()  # Save changes
            return redirect('core:appointments_list')
        else:
            print(form.errors)
    else:
        form = AppointmentForm()

    return render(request, 'core/appointment_form.html', {
        'form': form,
        'form_title': 'Create New Appointment'
    })

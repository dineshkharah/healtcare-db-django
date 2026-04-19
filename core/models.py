from django.db import models
from django.contrib.auth.models import User

# Patient model
class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='patients'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Doctor model
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Patient-Doctor Mapping Model
class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='doctor_mappings'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='patient_mappings'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')  # prevent duplicate mapping

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
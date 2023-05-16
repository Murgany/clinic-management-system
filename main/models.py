from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

"""
The departments variable is a list of tuples that contains 
the names and abbreviations of the different medical departments that doctors belong to.
"""
departments = [
               ('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]


class Doctor(models.Model):
    """
    The Doctor class represents a doctor in the system. Each doctor has a name, address, phone number,
    department, and status.
    """
    user = models.OneToOneField(User, verbose_name=_("Doctor's Name"), on_delete=models.CASCADE)
    profile_picture = models.ImageField(_('Profile photo'), upload_to='profile_pic/', null=True, blank=True)
    address = models.CharField(_('Address'), max_length=40)
    mobile = models.CharField(_('Phone'), max_length=20, null=True)
    department = models.CharField(_('Speciality'), max_length=50, choices=departments, default='Cardiologist')
    status = models.BooleanField(default=False, verbose_name=_('Status: Active / Not active'))

    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')

    # Return a human-readable name
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Patient(models.Model):
    """
    The Patient class represents a patient in the system. Each patient has a name, age, gender,
    address, phone number, symptoms, diagnosis, treatment, doctor, and next appointment.
    """
    # doctor = models.ManyToManyField(Doctor, default=User.first_name)
    doctor = models.CharField(_("Doctor's Name"), max_length=120, null=True)
    date = models.DateField(_('Date'), auto_now=True, blank=True)
    patient_name = models.CharField(_('Patient name'), max_length=100, null=False)
    age = models.PositiveIntegerField(_('Age'), null=True)

    GENDER_CHOICES = (
        ('M',  'M'),
        ('F',  'F'),
    )

    gender = models.CharField(_('Gender'), choices=GENDER_CHOICES, max_length=20, default='M')
    address = models.CharField(_('Address'), max_length=40, blank=True)
    mobile = models.CharField(_('Phone'), max_length=20, blank=True, null=False)
    symptoms = models.CharField(_('Symptoms'), max_length=5000, null=False)
    diagnosis = models.CharField(_('Diagnosis'), max_length=5000)
    treatment = models.CharField(_('Treatment'), max_length=5000)
    doctors_comment = models.CharField(_('Doctors comment'), max_length=5000)
    next_appointment = models.DateField(_('Next appointment'), auto_now=False, blank=True, null=True)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')

    # Return a human-readable name
    def __str__(self):
        return self.patient_name


class SpecialSession(models.Model):
    """
    The SpecialSession class represents a special session that a patient can attend.
    Each special session has a date,doctor, patient, symptoms, diagnosis, treatment,
    and next appointment.
    """
    doctor = models.CharField(_("Doctor's Name"), max_length=120, null=True)
    date = models.DateField(_('Date'), auto_now=True, blank=True)
    patient_name = models.CharField(_('Patient name'), max_length=100, null=False)
    age = models.PositiveIntegerField(_('Age'), null=True)

    GENDER_CHOICES = (
        ('M',  'M'),
        ('F',  'F'),
    )

    gender = models.CharField(_('Gender'), choices=GENDER_CHOICES, max_length=20, default='M')
    address = models.CharField(_('Address'), max_length=40, blank=True)
    mobile = models.CharField(_('Phone'), max_length=20, blank=True, null=False)
    symptoms = models.CharField(_('Symptoms'), max_length=5000, null=False)
    diagnosis = models.CharField(_('Diagnosis'), max_length=5000)
    treatment = models.CharField(_('Treatment'), max_length=5000)
    doctors_comment = models.CharField(_('Doctors comment'), max_length=5000)
    next_appointment = models.DateField(_('Next appointment'), auto_now=False, blank=True, null=True)

    class Meta:
        verbose_name = _('Special Session')
        verbose_name_plural = _('Special Sessions')

    # Return a human-readable name
    def __str__(self):
        return self.patient_name


class Appointment(models.Model):
    """
    The Appointment class represents an appointment that a patient has with a doctor.
    Each appointment has a date, date of appointment, doctor, department, patient, age,
    gender, address, phone number, and description.
    """
    date = models.DateField(_('Date'), auto_now=True)
    date_of_appointment = models.DateTimeField(_('Date of appointment'), auto_now_add=False, null=False)
    doctor = models.ManyToManyField(Doctor, verbose_name=_("Doctor's Name"), max_length=100)
    department = models.CharField(_('Speciality'), max_length=50, choices=departments, default='Cardiologist')
    patient_full_name = models.CharField(_('Patient name'), max_length=100, null=True)
    age = models.PositiveIntegerField(_('Age'), null=True)

    GENDER_CHOICES = (
        ("M",  "Male"),
        ("F",  "Female"),
    )

    gender = models.CharField(_('Gender'), choices=GENDER_CHOICES, max_length=20, default="M")
    address = models.CharField(_('Address'), max_length=40, blank=True)
    mobile = models.CharField(_('Mobile'), max_length=20, blank=True, null=False)
    description = models.CharField(_('Description'), max_length=300, blank=True)

    class Meta:
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')

    # Return a human-readable name
    def __str__(self):
        return self.patient_full_name


# Developed: by Rawy Murgany.
# LinkedIn: https://www.linkedin.com/in/rawy-mo

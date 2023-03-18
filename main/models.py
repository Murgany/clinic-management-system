from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]

class Doctor(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    profile_picture = models.ImageField(_('Profile photo'), upload_to='profile_pic/', null=True, blank=True)
    address = models.CharField(_('Address'), max_length=40)
    mobile = models.CharField(_('Phone'), max_length=20, null=True)
    department = models.CharField(_('Speciality'), max_length=50, choices=departments, default='Cardiologist')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id
    
    class Meta:
        verbose_name = _('Doctor')
        verbose_name_plural = _('Doctors')

    def __str__(self):
        return f"{self.user.first_name}, ({self.department})"


class Patient(models.Model):
    # doctor = models.ManyToManyField(Doctor, default=User.first_name)
    doctor = models.CharField(_('Doctor'), max_length=120, null=True)
    date = models.DateField(_('Date'), auto_now=True, blank=True)
    # doctor_id = models.PositiveIntegerField(null=True)
    patient_name = models.CharField(_('Patient name'), max_length=100, null=False)
    age = models.PositiveIntegerField(_('Age'), null=True)

    GENDER_CHOICES = (
        ('M',  'M'),
        ('F',  'F'),
    )

    gender = models.CharField(_('Gender'), choices=GENDER_CHOICES, max_length=20, default='M')
    # profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    address = models.CharField(_('Address'), max_length=40, blank=True)
    mobile = models.CharField(_('Phone'), max_length=20, blank=True, null=False)
    symptoms = models.CharField(_('Symptoms'), max_length=5000, null=False)
    diagnosis = models.CharField(_('Diagnosis'), max_length=5000)
    treatment = models.CharField(_('Treatment'), max_length=5000)
    doctors_comment = models.CharField(_('Doctors comment'), max_length=5000)
    next_appointment = models.DateField(_('Next appointment'), auto_now=False, blank=True, null=True)
    # status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.patient_name

    # @property
    # def get_id(self):
    #     return self.user.id
    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')

    def __str__(self):
        return self.patient_name


class Appointment(models.Model):
    date = models.DateField(_('Date'), auto_now=True)
    date_of_appointment = models.DateTimeField(_('Date of appointment'), auto_now_add=False, null=False)
    # doctor = models.OneToOneField(Doctor, auto_created=True ,on_delete=models.CASCADE, null=True)
    doctor = models.ManyToManyField(_('Doctor'), max_length=100, null=True)
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
    description = models.TextField(_('Description'), max_length=1000, blank=True)


    class Meta:
        verbose_name = _('Appointment')
        verbose_name_plural = _('Appointments')
    

    def __str__(self):
        return self.patient_full_name


class PatientSummary(Patient):
    class Meta:
        proxy = True
        managed = False
        verbose_name = _('Summary')
        verbose_name_plural = _('Summary')

# Developed: by Rawy Murgany.
# LinkedIn: https://www.linkedin.com/in/rawy-mo


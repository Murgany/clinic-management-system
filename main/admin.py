from django.contrib import admin
from .models import Doctor, Patient, Appointment, SpecialSession
from django.contrib.auth.models import User, Group
from django.forms import Textarea


# models set up | to be registered to the django admin site

class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'age', 'gender', 'mobile', 'date', 'next_appointment', 'doctor']
    search_fields = ['patient_name', 'doctor']


class SpecialSessionAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'age', 'gender', 'mobile', 'date', 'next_appointment', 'doctor']
    search_fields = ['patient_name', 'doctor']


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_full_name', 'age', 'gender', 'mobile', 'date_of_appointment', 'description', ]
    search_fields = ['patient_full_name', 'date_of_appointment']

    class Meta:
        model = Appointment
        widgets = {
            'parameters': Textarea(attrs={'cols': 12, 'rows': 5}),
        }


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'mobile', 'status']
    search_fields = ['user', 'department']


# register the models to django admin site
admin.site.register(Patient, PatientAdmin)
admin.site.register(SpecialSession, SpecialSessionAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Doctor, DoctorAdmin)

# Specify the ordering of the models in the admin site
admin.site.ordering = [PatientAdmin, SpecialSessionAdmin, AppointmentAdmin, DoctorAdmin]

# admin.site.unregister(User)
admin.site.unregister(Group)
# admin.site.unregister(admin_tools_stats)

# activate the app index dashboard
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'demoproject.dashboard.CustomAppIndexDashboard'

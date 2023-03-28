from django.contrib import admin
from .models import Doctor, Patient, Appointment, PatientSummary
from django.contrib.auth.models import User, Group


class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'age', 'gender', 'mobile', 'date', 'next_appointment', 'doctor',]
    search_fields = ['patient_name', 'doctor']

    

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'mobile', 'status']
    search_fields = ['user', 'department']


class AppointmentAdmin(admin.ModelAdmin):
      list_display = ['patient_full_name', 'age', 'gender', 'mobile', 'date_of_appointment', 'description', ]
      search_fields = ['patient_full_name', 'date_of_appointment']
    #   list_select_related = ['doctor']
    #   list_display_links = ['doctor']

    # list_display_links = ['name']
  
    #   def get_tags(self):
    #       return [tag.name for tag in instance.tags.all()]
      


class PatientSummaryAdmin(admin.ModelAdmin):
        # class ResultsAdmin(admin.ModelAdmin):
    # search_fields = ['body', 'question__survey__name', 'question__text', 'question__correct_answer__correct_ans']
    date_hierarchy = "date"
    # change_list_template = '/admin/c.html'
    # list_per_page = 10

    def changelist_view(self, request, extra_context=None):
        response = super(PatientSummaryAdmin, self).changelist_view(request, extra_context=extra_context)
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        from django.db.models import Count, Sum
        metrics = {
            'total': Count('id'),
            'total_patients': Count('patient_name'),
        }

        response.context_data['summary'] = list(
            qs.values('patient_name').annotate(**metrics).order_by('-total_patients')
        )

        response.context_data['summary_total'] = dict(
            qs.aggregate(total=Count('patient_name'))
        )

        return response

    # # removes the 'Add' button from the list display
    # def has_add_permission(self, request, obj=None):
    #     return False

    # # removes the edit feature from the form_change display. content is read only.
    # def has_change_permission(self, request, obj=None):
    #     return False

        # response = super().changelist_view(
        #     request,
        #     extra_context=extra_context,
        # )

        # try:
        #     qs = response.context_data['cl'].queryset
        # except (AttributeError, KeyError):
        #     return response
        

    # def get_queryset(self, request):
        # from django.db.models import Count, Sum
    #     queryset = super().get_queryset(request)
    #     queryset = queryset.annotate(patient_count=Count("patient_name"))
    #     return queryset

        # metrics = {
        #     'total': Count('patient_name'),
        #     # 'total_patients': Sum('patient_name'),
        # }

        # response.context_data['summary'] = list(
        #     qs.annotate(Count('patient_name'))
        # )

        # return response

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
# admin.site.register(PatientSummary, PatientSummaryAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
# admin.site.unregister(admin_tools_stats)


# to activate the app index dashboard::
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'demoproject.dashboard.CustomAppIndexDashboard'


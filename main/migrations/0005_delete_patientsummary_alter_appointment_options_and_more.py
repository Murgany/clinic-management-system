# Generated by Django 4.1.7 on 2023-03-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_patientsummary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientSummary',
        ),
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Appointment', 'verbose_name_plural': 'Appointments'},
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'Doctor', 'verbose_name_plural': 'Doctors'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Patient', 'verbose_name_plural': 'Patients'},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='address',
            field=models.CharField(blank=True, max_length=40, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_of_appointment',
            field=models.DateField(verbose_name='Date of appointment'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50, verbose_name='Speciality'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Description'),
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=20, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_full_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Patient name'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=40, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50, verbose_name='Speciality'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.CharField(max_length=20, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/', verbose_name='Profile photo'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=40, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='diagnosis',
            field=models.CharField(max_length=5000, verbose_name='Diagnosis'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.CharField(max_length=120, null=True, verbose_name='Doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctors_comment',
            field=models.CharField(max_length=5000, verbose_name='Doctors comment'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=20, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_appointment',
            field=models.DateField(blank=True, null=True, verbose_name='Next appointment'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_name',
            field=models.CharField(max_length=100, verbose_name='Patient name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(max_length=5000, verbose_name='Symptoms'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='treatment',
            field=models.CharField(max_length=5000, verbose_name='Treatment'),
        ),
        migrations.CreateModel(
            name='PatientSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Summary',
                'verbose_name_plural': 'Summary',
                'managed': False,
                'proxy': True,
            },
            bases=('main.patient',),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ManyToManyField(max_length=100, null=True, to='main.doctor'),
        ),
    ]

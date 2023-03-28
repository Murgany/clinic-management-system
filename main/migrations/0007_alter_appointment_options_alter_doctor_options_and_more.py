# Generated by Django 4.1.7 on 2023-03-26 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_alter_appointment_date_of_appointment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'مقابلة', 'verbose_name_plural': 'المقابلات'},
        ),
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'Doctor', 'verbose_name_plural': 'الدكاترة'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'مريض', 'verbose_name_plural': 'المرضى'},
        ),
        migrations.AlterModelOptions(
            name='patientsummary',
            options={'managed': False, 'verbose_name': 'ملخص', 'verbose_name_plural': 'ملخص'},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='address',
            field=models.CharField(blank=True, max_length=40, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='العمر'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='التاريخ'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_of_appointment',
            field=models.DateTimeField(verbose_name='تاريخ المقابلة'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50, verbose_name='التخصص'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.TextField(blank=True, max_length=1000, verbose_name='شرح'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ManyToManyField(max_length=100, null=True, to='main.doctor', verbose_name="Doctor's Name"),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=20, verbose_name='النوع'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, verbose_name='موبايل'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_full_name',
            field=models.CharField(max_length=100, null=True, verbose_name='اسم المريض'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=40, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50, verbose_name='التخصص'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.CharField(max_length=20, null=True, verbose_name='موبايل'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/', verbose_name='صورة شخصية'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status: Active / Not active'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Doctor's Name"),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=40, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='العمر'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='التاريخ'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='diagnosis',
            field=models.CharField(max_length=5000, verbose_name='التشخيص'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.CharField(max_length=120, null=True, verbose_name="Doctor's Name"),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctors_comment',
            field=models.CharField(max_length=5000, verbose_name='تعليق الطبيب'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=20, verbose_name='النوع'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, verbose_name='موبايل'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_appointment',
            field=models.DateField(blank=True, null=True, verbose_name='المقابلة القادمة'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_name',
            field=models.CharField(max_length=100, verbose_name='اسم المريض'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(max_length=5000, verbose_name='الاعراض'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='treatment',
            field=models.CharField(max_length=5000, verbose_name='العلاج'),
        ),
    ]

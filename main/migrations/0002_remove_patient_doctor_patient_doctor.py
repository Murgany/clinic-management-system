# Generated by Django 4.1.7 on 2023-03-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ManyToManyField(auto_created=True, to='main.doctor'),
        ),
    ]

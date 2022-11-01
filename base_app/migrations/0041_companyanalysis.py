# Generated by Django 4.1 on 2022-10-17 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0040_webpagecontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_date', models.DateField(blank=True, null=True)),
                ('analysis_compname', models.CharField(blank=True, max_length=150, null=True)),
                ('analysis_Employeeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
                ('analysis_taskid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.dm_project_task')),
            ],
        ),
    ]

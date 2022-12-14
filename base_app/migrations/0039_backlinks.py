# Generated by Django 4.1 on 2022-10-17 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0038_alter_datacollect_project_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backlinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bd_date', models.DateField(blank=True, null=True)),
                ('bd_url', models.URLField()),
                ('bd_type', models.CharField(blank=True, max_length=150, null=True)),
                ('bd_status', models.CharField(blank=True, max_length=50, null=True)),
                ('bd_Employeeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
                ('bd_taskid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.dm_project_task')),
            ],
        ),
    ]

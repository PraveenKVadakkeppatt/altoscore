# Generated by Django 4.1 on 2022-10-17 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0044_blogcalander'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmmPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smm_date', models.DateField(blank=True, null=True)),
                ('smm_sub', models.CharField(blank=True, max_length=100, null=True)),
                ('smm_type', models.CharField(blank=True, max_length=50, null=True)),
                ('smm_content', models.TextField()),
                ('smm_dese', models.TextField()),
                ('smm_satus', models.CharField(blank=True, max_length=50, null=True)),
                ('smm_file', models.ImageField(null=True, upload_to='poster')),
                ('smm_Employeeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
                ('smm_taskid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.dm_project_task')),
            ],
        ),
    ]
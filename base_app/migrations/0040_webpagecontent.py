# Generated by Django 4.1 on 2022-10-17 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0039_backlinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebpageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_date', models.DateField(blank=True, null=True)),
                ('web_url', models.URLField()),
                ('web_dese', models.TextField()),
                ('web_key', models.TextField()),
                ('web_Employeeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.user_registration')),
                ('web_taskid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.dm_project_task')),
            ],
        ),
    ]

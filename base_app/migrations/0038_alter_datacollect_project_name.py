# Generated by Django 4.1 on 2022-10-17 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0037_datacollect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datacollect',
            name='Project_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.dm_project_task'),
        ),
    ]

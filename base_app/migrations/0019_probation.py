# Generated by Django 3.2.12 on 2022-04-28 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0018_trainer_task_task_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='probation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('reason', models.TextField()),
                ('stop_reason', models.TextField(default='')),
                ('extension', models.IntegerField(default=0)),
                ('stopdate', models.DateField(blank=True, null=True)),
                ('renewdate', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(default=0)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_team', to='base_app.create_team')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_trainer', to='base_app.user_registration')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_user', to='base_app.user_registration')),
            ],
            options={
                'get_latest_by': ['status'],
            },
        ),
    ]

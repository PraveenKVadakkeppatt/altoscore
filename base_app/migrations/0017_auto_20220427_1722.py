# Generated by Django 3.2.12 on 2022-04-27 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0016_user_registration_hr_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_team',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='create_team',
            name='startdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='git_link',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='test_status',
            name='git_commit',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='test_status',
            name='git_link',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='reg_status',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='trainee_delay',
            field=models.IntegerField(default=0),
        ),
    ]

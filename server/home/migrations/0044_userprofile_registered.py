# Generated by Django 3.1.7 on 2021-09-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_centralredirection_redirect_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='registered',
            field=models.BooleanField(default=True),
        ),
    ]

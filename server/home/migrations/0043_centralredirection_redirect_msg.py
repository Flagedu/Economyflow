# Generated by Django 3.1.7 on 2021-07-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20210729_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='centralredirection',
            name='redirect_msg',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

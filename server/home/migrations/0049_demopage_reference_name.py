# Generated by Django 3.1.7 on 2021-09-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_auto_20210929_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='demopage',
            name='reference_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
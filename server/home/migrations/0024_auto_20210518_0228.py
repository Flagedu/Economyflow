# Generated by Django 3.1.7 on 2021-05-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20210518_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evestpage',
            name='template_choice',
            field=models.CharField(choices=[('ramadan', 'Ramadan'), ('islamic', 'Islamic'), ('ef05', 'Ef05'), ('ef06', 'Ef06')], default='ramadan', max_length=100),
        ),
    ]

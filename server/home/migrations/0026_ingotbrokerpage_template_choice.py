# Generated by Django 3.1.7 on 2021-05-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20210520_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingotbrokerpage',
            name='template_choice',
            field=models.CharField(choices=[('camp1', 'Campaign 1')], default='camp1', max_length=100),
        ),
    ]

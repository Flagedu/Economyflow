# Generated by Django 3.1.7 on 2021-09-26 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_buttoncountries_buttonlink_buttonrules'),
    ]

    operations = [
        migrations.AddField(
            model_name='demopage',
            name='investment_plan_link',
            field=models.URLField(max_length=250, null=True),
        ),
    ]

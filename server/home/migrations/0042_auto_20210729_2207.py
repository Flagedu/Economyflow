# Generated by Django 3.1.7 on 2021-07-29 16:07

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_centralredirection_accepted_param'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evestpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], blank=True, null=True),
        ),
    ]
# Generated by Django 3.1.7 on 2021-07-03 03:20

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_evestpage_allowed_countries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evestpage',
            name='allowed_countries',
        ),
        migrations.AddField(
            model_name='evestpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirection', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], null=True),
        ),
    ]
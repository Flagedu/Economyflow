# Generated by Django 3.1.7 on 2021-07-03 05:06

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20210703_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingotbrokerpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], null=True),
        ),
        migrations.AddField(
            model_name='legacyfxpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], null=True),
        ),
        migrations.AlterField(
            model_name='evestpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], null=True),
        ),
    ]

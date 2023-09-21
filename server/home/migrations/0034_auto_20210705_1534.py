# Generated by Django 3.1.7 on 2021-07-05 09:34

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_tradersgccpage_redirection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evestpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules, required=False))]))], null=True),
        ),
        migrations.AlterField(
            model_name='ingotbrokerpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules, required=False))]))], null=True),
        ),
        migrations.AlterField(
            model_name='legacyfxpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules, required=False))]))], null=True),
        ),
        migrations.AlterField(
            model_name='tradersgccpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules, required=False))]))], null=True),
        ),
    ]
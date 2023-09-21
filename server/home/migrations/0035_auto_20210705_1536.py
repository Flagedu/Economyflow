# Generated by Django 3.1.7 on 2021-07-05 09:36

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20210705_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evestpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], null=True),
        ),
        migrations.AlterField(
            model_name='ingotbrokerpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], null=True),
        ),
        migrations.AlterField(
            model_name='legacyfxpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], null=True),
        ),
        migrations.AlterField(
            model_name='tradersgccpage',
            name='redirection',
            field=wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], blank=True, null=True),
        ),
    ]
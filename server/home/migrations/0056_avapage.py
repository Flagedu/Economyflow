# Generated by Django 3.1.7 on 2022-04-06 20:05

from django.db import migrations, models
import django.db.models.deletion
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0055_centralcountries'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvaPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('template_choice', models.CharField(choices=[('ramadan', 'Ramadan')], default='ramadan', max_length=100)),
                ('parameters', models.CharField(blank=True, max_length=255, null=True)),
                ('redirection', wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]

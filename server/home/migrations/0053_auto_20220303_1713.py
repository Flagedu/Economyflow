# Generated by Django 3.1.7 on 2022-03-03 11:13

from django.db import migrations, models
import django.db.models.deletion
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
        ('home', '0052_auto_20211213_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapitalPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('template_choice', models.CharField(choices=[('starter-template', 'Starter Template')], default='starter-template', max_length=100)),
                ('parameters', models.CharField(blank=True, max_length=255, null=True)),
                ('redirection', wagtail.core.fields.StreamField([('redirection', wagtail.core.blocks.StructBlock([('redirect', wagtail.core.blocks.ListBlock(home.blocks.RedirectRules))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='apiregistration',
            name='type',
            field=models.CharField(choices=[('evest', 'Evest'), ('trade360', 'Trade360'), ('legacyfx', 'LegacyFx'), ('ingot', 'Ingot'), ('alvexo', 'Alvexo'), ('axia', 'Axia'), ('capital', 'Capital')], default='evest', max_length=50),
        ),
        migrations.AlterField(
            model_name='redirection',
            name='page_type',
            field=models.CharField(choices=[('evest', 'Evest'), ('trade360', 'Trade360'), ('legacyfx', 'LegacyFx'), ('ingot', 'Ingot'), ('alvexo', 'Alvexo'), ('axia', 'Axia'), ('capital', 'Capital')], default='evest', max_length=100),
        ),
    ]

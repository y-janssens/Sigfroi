# Generated by Django 4.0.3 on 2022-05-15 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0019_alter_aliase_options_alter_aliasessheet_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charactersheet',
            name='has_aliases',
        ),
    ]

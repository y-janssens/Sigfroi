# Generated by Django 4.0.3 on 2022-06-07 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0021_alter_skillsheet_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skillsheet',
            options={'ordering': ['skill']},
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-07 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0023_alter_charactersheet_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charactersheet',
            options={'ordering': ['name']},
        ),
    ]

# Generated by Django 4.0.3 on 2022-08-13 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0008_armoryweaponsnotes_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArmoryWeaponsNotes',
            new_name='ArmoryWeaponsNote',
        ),
    ]
# Generated by Django 4.1 on 2022-11-13 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0026_alter_charactersheet_is_active'),
        ('cartes', '0005_remove_card_avatar'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cardsheet',
            unique_together={('owner', 'card')},
        ),
    ]

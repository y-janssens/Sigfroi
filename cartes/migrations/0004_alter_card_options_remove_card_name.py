# Generated by Django 4.0.3 on 2022-05-20 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartes', '0003_card_ref'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['ref']},
        ),
        migrations.RemoveField(
            model_name='card',
            name='name',
        ),
    ]

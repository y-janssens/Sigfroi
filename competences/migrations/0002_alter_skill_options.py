# Generated by Django 4.0.3 on 2022-04-29 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['name']},
        ),
    ]

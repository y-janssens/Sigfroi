# Generated by Django 4.0.3 on 2022-04-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0006_skill_level'),
        ('fiches', '0004_alter_charactersheet_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactersheet',
            name='skills',
            field=models.ManyToManyField(to='competences.skill'),
        ),
    ]

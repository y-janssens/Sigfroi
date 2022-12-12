# Generated by Django 4.1 on 2022-11-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0023_alter_skillsheet_unique_together'),
        ('fiches', '0026_alter_charactersheet_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactersheet',
            name='skill_set',
            field=models.ManyToManyField(blank=True, to='competences.skillsheet'),
        ),
    ]
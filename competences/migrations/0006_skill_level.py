# Generated by Django 4.0.3 on 2022-04-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0005_alter_skill_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='level',
            field=models.TextField(blank=True, choices=[('Niveau 1', 'Niveau 1'), ('Niveau 2', 'Niveau 2'), ('Niveau 3', 'Niveau 3')], default='Niveau 1', max_length=100, null=True),
        ),
    ]

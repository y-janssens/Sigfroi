# Generated by Django 4.0.3 on 2022-05-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0018_alter_skillsheet_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillsheet',
            name='level',
            field=models.CharField(choices=[('Unique', 'Unique'), ('Niveau 1', 'Niveau 1'), ('Niveau 2', 'Niveau 2'), ('Niveau 3', 'Niveau 3')], default='Niveau 1', max_length=50),
        ),
    ]

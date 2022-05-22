# Generated by Django 4.0.3 on 2022-04-30 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0010_remove_skillsheet_skills_skillsheet_i_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='level',
        ),
        migrations.RemoveField(
            model_name='skillsheet',
            name='i',
        ),
        migrations.AddField(
            model_name='skillsheet',
            name='level',
            field=models.CharField(blank=True, choices=[('Non-Acquis', 'Non-Acquis'), ('Unique', 'Unique'), ('Niveau 1', 'Niveau 1'), ('Niveau 2', 'Niveau 2'), ('Niveau 3', 'Niveau 3')], default='Non-Acquis', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='skillsheet',
            name='owned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='skillsheet',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competences.skill'),
        ),
    ]

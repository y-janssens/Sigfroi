# Generated by Django 4.0.3 on 2022-04-29 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fiches', '0004_alter_charactersheet_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('level', models.CharField(blank=True, choices=[('Niveau 1', 'Niveau 1'), ('Niveau 2', 'Niveau 2'), ('Niveau 3', 'Niveau 3')], default='Niveau 1', max_length=50, null=True)),
                ('text', models.TextField(blank=True, max_length=500, null=True)),
                ('owner', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='fiches.charactersheet')),
            ],
        ),
    ]

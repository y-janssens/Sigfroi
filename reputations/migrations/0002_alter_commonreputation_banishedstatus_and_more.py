# Generated by Django 4.0.3 on 2022-04-23 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonreputation',
            name='banishedStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonreputation',
            name='clergyStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonreputation',
            name='globalStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonreputation',
            name='guildStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonreputation',
            name='kingStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonreputation',
            name='labretStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonreputation',
            name='mafiaStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonreputation',
            name='militiaStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonreputation',
            name='nobilityStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonreputation',
            name='peopleStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='commonreputation',
            name='sombreboisStatus',
            field=models.CharField(blank=True, choices=[('Excellente', 'Excellente'), ('Positive', 'Positive'), ('Neutre', 'Neutre'), ('Négative', 'Négative'), ('Recherché', 'Recherché'), ('Banni(e)', 'Banni(e)')], default='Neutre', max_length=50, null=True),
        ),
    ]

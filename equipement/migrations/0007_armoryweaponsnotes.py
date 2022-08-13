# Generated by Django 4.0.3 on 2022-08-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0006_alter_stuffsheet_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmoryWeaponsNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, max_length=2000, null=True)),
                ('type', models.CharField(blank=True, choices=[('list', 'list'), ('global', 'global')], default='list', max_length=50, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0020_remove_charactersheet_has_aliases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactersheet',
            name='is_active',
            field=models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Oui', max_length=50, null=True),
        ),
    ]

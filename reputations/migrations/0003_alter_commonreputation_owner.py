# Generated by Django 4.0.3 on 2022-04-23 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0003_charactersheet_member'),
        ('reputations', '0002_alter_commonreputation_banishedstatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonreputation',
            name='owner',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='fiches.charactersheet'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-29 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0023_alter_charactersheet_avatar'),
        ('succes', '0003_rename_success_1_achievementssheet_succes_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievementssheet',
            name='owner',
            field=models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, to='fiches.charactersheet'),
        ),
    ]

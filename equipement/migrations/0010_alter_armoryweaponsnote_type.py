# Generated by Django 4.0.3 on 2022-08-13 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipement', '0009_rename_armoryweaponsnotes_armoryweaponsnote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armoryweaponsnote',
            name='type',
            field=models.CharField(blank=True, choices=[('list', 'list'), ('global', 'global'), ('attr', 'attr')], default='list', max_length=50, null=True),
        ),
    ]

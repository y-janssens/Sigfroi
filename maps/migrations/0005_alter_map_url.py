# Generated by Django 4.1.4 on 2023-04-08 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_item_points_alter_item_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='url',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True, unique=True),
        ),
    ]

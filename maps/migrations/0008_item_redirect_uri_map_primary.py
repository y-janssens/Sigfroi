# Generated by Django 4.1.4 on 2024-02-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_item_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='redirect_uri',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='map',
            name='primary',
            field=models.BooleanField(default=False),
        ),
    ]

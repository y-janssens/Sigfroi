# Generated by Django 4.1 on 2022-12-23 13:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_progressbar_symbol_progressbar_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='progressbar',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]

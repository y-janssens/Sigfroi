# Generated by Django 4.0.3 on 2022-05-21 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0022_charactersheet_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactersheet',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default.png', null=True, upload_to='avatars'),
        ),
    ]

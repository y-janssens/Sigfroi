# Generated by Django 4.0.3 on 2022-05-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0016_alter_charactersheet_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactersheet',
            name='has_aliases',
            field=models.ManyToManyField(blank=True, null=True, to='fiches.charactersheet'),
        ),
    ]

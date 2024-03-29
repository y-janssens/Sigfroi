# Generated by Django 4.1 on 2022-09-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chroniques', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chronique',
            name='banished',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronique',
            name='characters',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronique',
            name='clergy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronique',
            name='militia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronique',
            name='nobles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chronique',
            name='people',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

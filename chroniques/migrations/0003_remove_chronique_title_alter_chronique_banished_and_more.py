# Generated by Django 4.1 on 2022-09-16 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chroniques', '0002_chronique_banished_chronique_characters_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chronique',
            name='title',
        ),
        migrations.AlterField(
            model_name='chronique',
            name='banished',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='chronique',
            name='characters',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='chronique',
            name='clergy',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='chronique',
            name='militia',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='chronique',
            name='nobles',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='chronique',
            name='people',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]

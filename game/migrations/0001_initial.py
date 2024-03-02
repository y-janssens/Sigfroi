# Generated by Django 4.1.4 on 2024-03-02 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='game')),
                ('created', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['created', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=255, unique=True)),
                ('url', models.CharField(blank=True, max_length=255)),
                ('text', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]

# Generated by Django 4.1.4 on 2023-04-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0006_alter_map_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(choices=[('#d0021b', '#d0021b'), ('#f5a623', '#f5a623'), ('#f8e71c', '#f8e71c'), ('#8b572a', '#8b572a'), ('#7ed321', '#7ed321'), ('#417505', '#417505'), ('#bd10e0', '#bd10e0'), ('#ff6900', '#ff6900'), ('#0032fa', '#0032fa'), ('#7bdcb5', '#7bdcb5'), ('#00d084', '#00d084'), ('#8ed1fc', '#8ed1fc'), ('#0693e3', '#0693e3'), ('#abb8c3', '#abb8c3'), ('#eb144c', '#eb144c'), ('#f78da7', '#f78da7')], default='#d0021b', max_length=7),
        ),
    ]

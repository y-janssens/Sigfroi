# Generated by Django 4.0.3 on 2022-05-15 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0018_aliase_alter_charactersheet_has_aliases_aliasessheet_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aliase',
            options={'ordering': ['owner']},
        ),
        migrations.AlterModelOptions(
            name='aliasessheet',
            options={'ordering': ['owner']},
        ),
        migrations.RenameField(
            model_name='aliase',
            old_name='name',
            new_name='owner',
        ),
    ]
